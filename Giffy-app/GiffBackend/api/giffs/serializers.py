from rest_framework import serializers
from .models import FavouriteGiffs
from api.users.models import CustomUser
from rest_framework.authtoken.models import Token

class GiffsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavouriteGiffs
        fields = ['giff_id' ,'added_at']

class UserGiffValidationSerializer(serializers.Serializer):
    
    username = serializers.CharField(max_length=50)
    token = serializers.CharField(max_length=50)

    def validate_username(self, value):
        user = CustomUser.objects.get(username = value)
        if user == None:
            raise serializers.ValidationError({'error':'Ha habido un problema con tu usuario!'})
        return value
    
    def validate_token(self, value):
        username_sent = self.context['username']
        user = CustomUser.objects.get(username = username_sent)
        token = Token.objects.get(user = user)
        if value != token.key:
            raise serializers.ValidationError({'error':'Tu sesión no es correcta'})
        
        return value
    
    def validate(self, data):
        print('validation')
        return data