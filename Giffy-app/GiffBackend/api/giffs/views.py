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

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from api.users.models import CustomUser
from .serializers import GiffsSerializer, UserGiffValidationSerializer


User = get_user_model()

# Create your views here.

class GiffApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request, *args, **kwargs):
        
        giff_list = FavouriteGiffs.objects.filter(user= request.user)

        serializer = GiffsSerializer(giff_list, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_fav_giffs(request, username,token,*args, **kwargs):
    
    if request.method == 'GET':
        
        try:
            user = CustomUser.objects.get(username = username)
            giff_list = FavouriteGiffs.objects.filter(user = user)
            
            giff_serializer = GiffsSerializer(giff_list, many=True)
            test_user = {
                'username':username,
                'token': token
            }
            my_user_serializer = UserGiffValidationSerializer(data = test_user, context = test_user)

            if my_user_serializer.is_valid():
                print('perfecto')
                return Response({'success':'Todo ha ido genial!'})

            return Response({'error':'Ha habido un error'})
            
        except CustomUser.DoesNotExist:
            return Response({'error':'Ha habido un problema. El usuario no existe!'})

        