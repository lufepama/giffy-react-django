from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.


class FavouriteGiffs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    giff_id = models.CharField(max_length = 100, blank =True, null = True)
    added_at = models.DateTimeField(auto_now_add=True)