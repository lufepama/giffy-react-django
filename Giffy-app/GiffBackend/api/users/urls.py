from django.urls import path, include
from .views import user_get_create_api, Login

urlpatterns = [
    # path('signup/', UserApiView.as_view()),
    path('signup/',user_get_create_api, name= 'create-get-user'),
    path('login/',Login.as_view(), name = 'login' )
]