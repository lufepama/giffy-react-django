from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from django.contrib.auth import login, logout
from rest_framework.permissions import AllowAny
from api.users.models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


class UserApiView(APIView):
    
    permission_classes = (AllowAny,)
    
    def post(self, request, format= None, *args, **kwargs):#Create new users
        
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        print(password)
        qs = User.objects.filter(username=username).first()

        if qs == None:

            if password == password1:
                new_user = User(
                    first_name = name, username = username, email = email, password = password
                )
                new_user.save()
            
                return Response({'success':'Has creado la cuenta correctamente ;)'})
            else:
                return Response({'error':'Las contraseñas no coinciden'})
        else:
            return Response({'error':'Ya existe un usuario con las mismas credenciales'})

class UserLoginApiView(APIView):
    
    def generate_session_token (self, length=10):
        return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length) )

    def post(self, request, *args, **kwargs):
        
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username = username)

            if user.password == password:
                if user.session_token == '0':
                    new_session_token = self.generate_session_token()
                    user.session_token = new_session_token
                    user.save()
                    login(request, user)
                    return Response({'success':'Has iniciado session correctamente'})

                else:
                    user.session_token = '0'
                    user.save()
                    return Response({'error':'Ya has iniciado sessión!'})
            else:
                return Response({'error':'Las credenciales no son correctas'})

        except User.DoesNotExist:
            return Response({'error':'El usuario no existe'})

class UserGetTokenApiView(APIView):
        
    def get(self, request, username, *args, **kwargs):
        
        try:
            user = User.objects.get(username= username)
            if user.is_authenticated:
                return Response({'success':'Ahi tienes!', 'token':user.session_token})
            else:
                return Response({'error':'El usuario no está autenticado'})

        except User.DoesNotExist:
            return Response({'error':'Ha habido un problema'})