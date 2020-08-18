from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView,RetrieveAPIView,RetrieveUpdateAPIView
from .serializers import UserRegisterSerializer,ProductSerializer,UserLoginSerializer
from datahandle.models import Product
from django.contrib.auth import login as django_login,logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

class UserRegisterCreateAPIView(CreateAPIView):
    serializer_class=UserRegisterSerializer

class UserLoginCreateView(APIView):
    def post(self,request):
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        django_login(request,user)
        token, created= Token.objects.get_or_create(user=user)
        return Response({'token':token.key},status=200)

class UserLogoutView(APIView):
    authentication_classes=(TokenAuthentication,)
    def post(self,request):
        django_logout(request)
        return Response(status=204)


class ProductsListView(ListAPIView):
    serializer_class= ProductSerializer
    queryset=Product.objects.all()

class ProductRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

    