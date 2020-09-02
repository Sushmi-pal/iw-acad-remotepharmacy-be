from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import LoginForm,RegisterForm
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes
from django.contrib.auth import authenticate,login,logout
User = get_user_model()
# Create your views here.


def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(phone=form.cleaned_data['phone'],
                                password=form.cleaned_data['password'])
            if user:
                print('user', user)
                login(request, user)
                return redirect('/users/main/')
            else:
                print('Not authenticated')
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/users/main/')
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('form is valid')
            user = User(phone=form.cleaned_data['phone'],
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'])
            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            print('user', user)
            return redirect('/users/login/')
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/users/main/')
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


def MainView(request):
    return render(request,'users/profile.html')

def LogoutView(request):
    logout(request)
    return redirect('/users/login/')

def adminorcustomer(request):
    if request.user.username=='121' and request.user.phone=='121':
        request.user.role=='admin'
        return request.user.role


@authentication_classes([TokenAuthentication])
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)