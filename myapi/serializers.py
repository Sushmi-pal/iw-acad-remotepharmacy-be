from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'phone')
        
from rest_framework import serializers
from datahandle.models import Category,Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','name','desc','image','price','in_stock']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    # products = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ('name','products')



