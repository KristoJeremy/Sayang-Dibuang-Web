from django.db import models
from django.contrib.auth.models import User
from fitur_autentikasi.models import Profile

class Message(models.Model):
    # Atirbut pesan
    random_message = models.TextField()
