from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('giffs/', include('api.giffs.urls')),
    path('users/', include('api.users.urls')),
]
