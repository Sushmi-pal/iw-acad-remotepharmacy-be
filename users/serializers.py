from rest_framework import serializers
from django.contrib.auth import get_user_model
User=get_user_model()

class ChangePasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField(required=True)
    new_password=serializers.CharField(required=True)

class ResetPasswordSerializer(serializers.Serializer):
    new_password=serializers.CharField(required=True)
    confirm_password=serializers.CharField(required=True)