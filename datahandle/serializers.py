from rest_framework import serializers
from .models import Category,Product, Cart, Order


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'desc', 'image', 'price', 'in_stock', 'category']


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    # products = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'products')


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['username', 'item', 'quantity', 'created_date']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['username', 'item', 'quantity', 'date', 'order_in_cart', 'ordered']
