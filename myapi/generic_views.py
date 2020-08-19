from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView,\
    DestroyAPIView, RetrieveAPIView,RetrieveUpdateAPIView
from .serializers import UserRegisterSerializer,ProductSerializer,UserLoginSerializer,CategorySerializer
from datahandle.models import Product,Category
from django.contrib.auth import login as django_login,logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from myapi.permissions import IsSuperUser
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