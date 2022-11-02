from email.policy import default
from django.db import models
from fitur_autentikasi.models import Profile
from django.contrib.auth.models import User
import datetime

class Review (models.Model):
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True, to_field="user"
    )
    judul = models.CharField(max_length = 255)
    deskripsi = models.TextField()
    created = models.DateTimeField(default = datetime.datetime.now())