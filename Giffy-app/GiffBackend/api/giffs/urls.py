from django.urls import path, include
from .views import GiffApiView

urlpatterns = [
    path('get-giff-list',GiffApiView.as_view())
]



