from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    line = models.CharField(max_length=100)
    poin = models.IntegerField(default=0)