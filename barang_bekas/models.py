from ast import mod
from email.policy import default
from enum import unique
from fitur_autentikasi.models import Profile
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Lokasi (models.Model):
    nama = models.CharField(max_length = 255, unique=True)

    def __str__(self):
        return self.nama 

class Kategori (models.Model):
    jenis =  models.CharField(max_length = 255, unique=True) 
    def __str__(self):
        return self.jenis

class Barang (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    foto = CloudinaryField("Image", overwrite=True, format="jpg")
    judul = models.CharField(max_length = 255)
    deskripsi = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add = True)
    lokasi = models.ForeignKey(Lokasi, on_delete=models.RESTRICT, to_field="nama")
    kategori = models.ForeignKey(Kategori, on_delete=models.RESTRICT, to_field="jenis")
    available = models.BooleanField(default=False) # menandakan masih available atau ga

    class Meta:
        # specify how we want the model to behave
        ordering=('-uploaded_at',) # order the models from recently created

    def __str__(self):
        return self.judul
