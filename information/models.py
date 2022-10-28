from django.db import models
from fitur_autentikasi.models import Profile
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Review (models.Model):
    # user = models.ForeignKey(
    #     Profile, on_delete=models.CASCADE, blank=True, null=True, to_field="user"
    # )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    judul = models.CharField(max_length = 255)
    deskripsi = HTMLField()
    created = models.DateTimeField(auto_now_add = True)

