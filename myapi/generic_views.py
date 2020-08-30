from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView,\
    DestroyAPIView, RetrieveAPIView,RetrieveUpdateAPIView
from .serializers import UserRegisterSerializer,ProductSerializer,UserLoginSerializer,\
    CategorySerializer
    # UserUpdateInfoSerializer
from rest_auth.serializers import  PasswordResetSerializer,PasswordResetConfirmSerializer
from datahandle.models import Product,Category
from django.contrib.auth import login as django_login,logout as django_logout
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from rest_framework import views, generics
from myapi.permissions import IsSuperUser
from .pagination import MyLimitOffsetPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import generics, mixins, permissions
from django.http import JsonResponse
from django.contrib.auth import get_user_model
User=get_user_model()

class UserRegisterCreateAPIView(CreateAPIView):
    serializer_class=UserRegisterSerializer


class UserLoginCreateView(APIView):
    def post(self,request):
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        django_login(request,user)
        token, created= Token.objects.get_or_create(user=user)
        return Response({'token':token.key,'id': token.user_id,'success':'You are logged in successfully'},status=200,
                        )

class UserLogoutView(APIView):
    authentication_classes=(TokenAuthentication,)
    def post(self,request):
        
        django_logout(request)
        return Response({'logout':'You are logged out'},status=204)

# class UserUpdateInfoView(generics.UpdateAPIView):
#     def get_obj(self):
#         return User.objects.get(id=Token.objects.get(key=self.request.auth.key).user_id)
#
#     queryset = User.objects.all()
#     serializer_class = UserUpdateInfoSerializer
#     permission_classes = [IsAuthenticated,]
#     authentication_class=[TokenAuthentication,]
#
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.username = request.data.get("username")
#         instance.save()
#
#         serializer = self.get_serializer(instance)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#
#         return Response(serializer.data)


    # def update(self, request, *args, **kwargs):
    #     if self.request.user:
    #         serializer = self.serializer_class(data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #
    #         return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsListView(ListAPIView):
    serializer_class= ProductSerializer
    queryset=Product.objects.all()
    pagination_class=MyLimitOffsetPagination
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['name']
    order_fields=['name','id']


class CategoryRetrieveView(RetrieveAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()


class ProductRetrieveView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    


class ProductUpdateView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperUser, ]

class ProductCreateAPIView(CreateAPIView):
    serializer_class=ProductSerializer
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperUser, ]

    def valid(self):
        return JsonResponse({'foo': 'bar'})



class ProductDeleteAPIView(DestroyAPIView):
    serializer_class=ProductSerializer
    queryset = Product.objects.all()
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperUser, ]

class CategoryCreateAPIView(CreateAPIView):
    serializer_class=CategorySerializer
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperUser, ]

class CategoryDeleteAPIView(DestroyAPIView):
    serializer_class=CategorySerializer
    queryset = Category.objects.all()
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperUser, ]

class CategoryListView(ListAPIView):
    serializer_class= CategorySerializer
    queryset=Category.objects.all()
    pagination_class = MyLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    order_fields = ['name', 'id']



# class UserUpdateInfoView(UpdateAPIView):
#     serializer_class=UserUpdateInfoSerializer
#     queryset=User.objects.all()
#     authentication_classes=[TokenAuthentication,]
#     permission_classes=[IsLoggedInUser,]



