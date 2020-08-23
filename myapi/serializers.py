from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate

User=get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','phone','role']
        
        
class UserRegisterSerializer(serializers.ModelSerializer):
    # role=serializers.SerializerMethodField(method_name='get_role')

    class Meta:
        model=User
        fields=['id','username','first_name','last_name','email','phone','password','confirm_password','role']
        extra_kwargs={'password':{'write_only':'True','required':'True'},
                        'confirm_password':{'write_only':'True','required':'True'}}



        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        validated_data['confirm_password'] = make_password(validated_data.get('confirm_password'))
        if validated_data['username']=='190' and validated_data['password']=='190':
            validated_data['role']=='admin'
            print(role)
        return super(UserRegisterSerializer, self).create(validated_data)

    def validate(self,data):
        password = data.get("password","")
        confirm_password = data.get("confirm_password","")

        if password != confirm_password:
            raise serializers.ValidationError('Password donot match')
        return data

    # def get_role(self, instance):
    #     request = self.context.get('request')
    #     user = request.user
    #     print(user.username)
    #     if instance.username=='queue':
    #         instance.role=='admin'
    #         instance.save()
    #
    #
    #         return 'admin'
    #     else:
    #         return 'customer'

    def update(self, **kwargs):
        instance = super().save(**kwargs)
        self.get_role(instance)
        instance.save()


    #
    # def validate(self,data):
    #     username=data.get("username","")
    #     phone=data.get("phone","")
    #     password=data.get("password","")
    #     confirm_password=data.get("confirm_password","")
    #     role=data.get("role","")
    #
    #     if username=="980" and phone=="980" and password=="admin" and confirm_password=="admin":
    #         raise ValidationError({'role':'admin'})
    #     return data



class UserLoginSerializer(serializers.Serializer):

    phone=serializers.CharField()
    password=serializers.CharField()
    token = serializers.CharField(max_length=68, min_length=6, read_only=True)

    def validate(self,data):

        phone = data.get("phone","")
        password = data.get("password","")
        
        if phone and password:

            user=authenticate(phone=phone,password=password)

            if user:
                
                if  user.is_active:
                    data['user']=user
                else:
                    raise exceptions.ValidationError("User is deactivated")

            else:
                raise serializers.ValidationError("Unable to login with given credentials")
        else:
            raise exceptions.ValidationError("Must provide phone and password")
        return data


class UserUpdateInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['id','username','first_name','last_name','email','phone']

from rest_framework import serializers
from datahandle.models import Category,Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','name','desc','image','price','in_stock','prod']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    # products = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','products']




# class UserInfoUpdateSerializer(serializers.ModelSerializer):
# 
#     class Meta:
#         model=User
#         fields=['id','username','first_name','last_name','email','phone']
# 

