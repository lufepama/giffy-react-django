from rest_framework import serializers
from .models import FavouriteGiffs

class GiffsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FavouriteGiffs
        fields = ['giff_id' ,'added_at']