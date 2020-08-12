from django.shortcuts import render
from .models import Product,Order,Cart,Category
from django.conrib.auth import get_user_model
User=get_user_model()
# Create your views here.

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


