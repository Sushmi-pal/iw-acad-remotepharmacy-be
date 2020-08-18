from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
User=get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','phone']
        
        
class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['id','username','first_name','last_name','email','phone','password','confirm_password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        validated_data['confirm_password'] = make_password(validated_data.get('confirm_password'))
        return super(UserRegisterSerializer, self).create(validated_data)

    def validate(self,data):
        password = data.get("password","")
        confirm_password = data.get("confirm_password","")

        if password != confirm_password:
            raise serializers.ValidationError('Password donot match')
        return data

class UserLoginSerializer(serializers.Serializer):

    phone=serializers.CharField()
    password=serializers.CharField()


    def validate(self,data):
        phone = data.get("phone","")
        password = data.get("password","")

        if phone and password:
            user=authenticate(phone=phone,password=password)
            if user:
                if user.is_active:
                    data['user']=user
                else:
                    raise exceptions.ValidationError("User is deactivated")

            else:
                raise exceptions.ValidationError("Unable to login with given credentials")
        else:
            raise exceptions.ValidationError("Must provide phone and password")
        return data




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



