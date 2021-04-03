from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny
from rest_framework import status

#Login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import UserTokenSerializer
from django.contrib.sessions.models import Session
from datetime import datetime

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def user_get_create_api(request, *args, **kwargs):
    
    if request.method == 'GET':

        users = CustomUser.objects.all()
        user_serializer = CustomUserSerializer(users, many = True)
        return Response(user_serializer.data)

    elif request.method == 'POST':
        new_user_serializer = CustomUserSerializer(data= request.data, context=request.data)
        
        if new_user_serializer.is_valid():
            new_user_serializer.save() #Create method need to be in serializer
            return Response({'success':'Cuenta creada satisfactoriamente'}, status = status.HTTP_200_OK)
        else:
            return Response(new_user_serializer.errors)

#Login
class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        #Will recieve data (username, password) from post
        
        login_serializer = self.serializer_class(data = request.data, context = {'request':request}) #Called AuthTokenSerializer. Contain 3 fields: username, password and Token
        print(login_serializer.is_valid())
        if login_serializer.is_valid():#Yes, it has username and password.
            #Once user is authenticated, it need to be logged in
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token':token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de session existoso'
                    }, status = status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte =datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decode()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()                   
                    #If user is logging from other place
                    token.delete()
                    token = Token.objects.create(user= user)
                    return Response({
                        'token':token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de session existoso'
                    }, status = status.HTTP_201_CREATED)
            else:
                return Response({'error':'El usuario no puede iniciar sesión'},
                                     status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'There was a problem'} )
