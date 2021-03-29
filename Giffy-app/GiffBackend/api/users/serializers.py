from rest_framework import serializers
from django.contrib.auth import password_validation, authenticate
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['email', 'created_at']
