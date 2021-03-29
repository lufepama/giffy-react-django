from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .serializers import GiffsSerializer
from django.contrib.auth import get_user_model
from .models import FavouriteGiffs
from .serializers import GiffsSerializer

User = get_user_model()

# Create your views here.

class GiffApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request, *args, **kwargs):
        
        giff_list = FavouriteGiffs.objects.filter(user= request.user)

        serializer = GiffsSerializer(giff_list, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
