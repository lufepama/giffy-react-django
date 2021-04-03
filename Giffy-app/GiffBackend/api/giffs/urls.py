from django.urls import path, include
from .views import GiffApiView, get_fav_giffs

urlpatterns = [
    path('get-giff-list/<str:username>/<str:token>/',get_fav_giffs, name='get-fav-giffs'),
]



