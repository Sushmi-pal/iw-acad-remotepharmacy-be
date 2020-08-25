from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer,ProductSerializer
from .models import Product,Order,Cart,Category
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from rest_framework import viewsets
from .serializers import CartSerializer, OrderSerializer
from .models import Cart
User = get_user_model()


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer


@api_view(['GET'])
def info_view_cat(request, pk):
    if request.method == 'GET':
        try:
            obj = Category.objects.get(id=pk)
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


def TotalPrice(request,user_id):
    user=User.objects.get(id=user_id)
    cartuser=user.cart_set.all()
    orderlist=[]
    for i in cartuser:
        orderlist.append[i.order_set.all()]
    countoforder=len(orderlist)
    loopcontroller=0
    sum=0
    while loopcontroller < len(countoforder):
        sum=sum+int(countoforder[loopcontroller].prod.price)
        s=s+1
    return render(request,'',{'sum':sum})


def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("template:home")    # put the location of home.html and it
                                                # redirects to where the home page is
        else:
            order.orderitems.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("template:home")
    else:
        order = Order.objects.create(
            user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("template:home")


def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.orderitems.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("template:home")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("template:home")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:home")
