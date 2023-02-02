from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Setting(models.Model):
    user = models.OneToOneField(User, verbose_name="user", on_delete=models.CASCADE)
    api_key = models.CharField(max_length=50)
    secret_key = models.CharField(max_length=50)
