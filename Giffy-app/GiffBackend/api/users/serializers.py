from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'email': instance.email
        }

class CustomUserSerializer(serializers.Serializer):
    #Fields that will be serialized
    username = serializers.CharField(max_length = 50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 20)
    
    def validate_username(self, value):
        
        try:
            current_user = CustomUser.objects.get(username = value)
            raise serializers.ValidationError({'error':'El nombre de usuario ya esta en uso. Elige otro :)!'}) 
        except:
            return value
    
    def validate(self, data):

        password = self.context['password']
        if password in self.context['username'] or password in self.context['email']:
            raise serializers.ValidationError({'error':'La contraseña no puede contener los campos de email o username'})

        return data

    def create(self, validated_data):
        #Encrypt password
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user