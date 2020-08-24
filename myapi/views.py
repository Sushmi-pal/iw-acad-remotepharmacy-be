from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.filters import SearchFilter,OrderingFilter
from django.contrib.auth import get_user_model
User=get_user_model()
from .pagination import MyLimitOffsetPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    pagination_class = MyLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username']
    order_fields = ['name', 'id']



from django.shortcuts import render
from datahandle.models import Product,Category
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from myapi.permissions import IsSuperUser
from rest_framework.response import Response
from rest_framework import status
from datahandle.serializers import CategorySerializer,ProductSerializer
from datahandle.models import Product,Order,Cart,Category
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.
@api_view(['GET'])
def info_view_cat(request,pk):
    if request.method=='GET':
        try:
            obj=Category.objects.get(id=pk)
            catprod = Product.objects.filter(prod=obj)
            b=[]
            for i in catprod:
                b.append(i)

            def produ():

                d=dict()
                l=[]
                for j in b:
                    d.update({'name':j.name ,
                              'desc':j.desc,
                              'image':j.image,
                              'price':j.price,
                              'in_stock':j.in_stock
                              },)
                    l.append(d)
                return l
            content={

                'name':produ,



            }


        except:
            return Response({'error':'Doesnot exists'})
        # queryset=Category.objects.all()
        # result=[]
        # for i in ram:
        #     serializer = InfoSerializer(instance=i)
        #     result.append(serializer.data)
        serializer=CategorySerializer(instance=content)

        return Response(serializer.data)

@api_view(['GET'])
def info_view(request):
    if request.method=='GET':
        queryset=Category.objects.all()
        serializer=CategorySerializer(instance=queryset,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def info_product_view(request):
    if request.method=='GET':
        queryset=Product.objects.all()
        # result=[]
        # for i in ram:
        #     serializer = InfoSerializer(instance=i)
        #     result.append(serializer.data)
        serializer=ProductSerializer(instance=queryset,many=True)

        return Response(serializer.data)

@api_view(['GET'])
def info_view_prod(request,pk):
    if request.method=='GET':
        try:
            obj=Category.objects.get(id=pk)
            catprod=Product.objects.get(prod=obj)
        except:
            return Response({'error':'Doesnot exists'})
        # queryset=Category.objects.all()
        # result=[]
        # for i in ram:
        #     serializer = InfoSerializer(instance=i)
        #     result.append(serializer.data)
        serializer=CategorySerializer(instance=catprod)

        return Response(serializer.data)


@api_view(['GET'])
def info_view_prodindividual(request,pk):
    if request.method=='GET':
        try:
            obj=Product.objects.filter(id=pk)
            def productind():

                d=dict()
                l=[]
                for j in obj:
                    d.update({'name':j.name ,
                              'desc':j.desc,
                              'image':j.image,
                              'price':j.price,
                              'in_stock':j.in_stock
                              },)
                    l.append(d)
                return l

            content = {

                'name': productind,

            }
        except:
            return Response({'error':'Doesnot exists'})
        serializer=CategorySerializer(instance=content)

        return Response(serializer.data)


# @api_view(['POST'])
# def UserRegisterCreateAPIView(request):
#     if request.method=='POST':
#         s=UserRegisterSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=201)
#         else:
#             return Response(s.data,status=203)
#     else:
#         return Response("",status=404)


@api_view(['DELETE', ])
@authentication_classes([TokenAuthentication])
@permission_classes([IsSuperUser])
def product_delete(request,pk):
    try:
        product=Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='DELETE':
        operation=product.delete()
        data={}
        if operation:
            data['success']='Deleted successfully'
        else:
            data['error']='Delete failed'
        return Response(data=data)

@api_view(['PUT', 'PATCH',])
@authentication_classes([TokenAuthentication])
@permission_classes([IsSuperUser])
def product_update(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer=ProductSerializer(product,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Updated successfully'
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer=ProductSerializer(product,data=request.data,partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Updated successfully'
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE', ])
@authentication_classes([TokenAuthentication])
@permission_classes([IsSuperUser])
def category_delete(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = category.delete()
        data = {}
        if operation:
            data['success'] = 'Deleted successfully'
        else:
            data['error'] = 'Delete failed'
        return Response(data=data)