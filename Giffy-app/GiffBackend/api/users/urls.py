from django.urls import path, include
from .views import UserApiView, UserLoginApiView, UserGetTokenApiView

urlpatterns = [
    path('signup/', UserApiView.as_view()),
    path('login/',UserLoginApiView.as_view()),
    path('get-token/', UserGetTokenApiView.as_view()),
]