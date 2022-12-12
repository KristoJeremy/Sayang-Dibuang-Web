from fitur_autentikasi.models import Profile
from django.db import models
from django.contrib.auth.models import User
from barang_bekas.models import Kategori

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    nama_barang = models.CharField(max_length = 255)
    deskripsi = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add = True)
    kategori = models.ForeignKey(Kategori, on_delete=models.RESTRICT, to_field="jenis")
    available = models.BooleanField(default=False)

    class Meta:
        ordering=("-uploaded_at",)

class RequestMobile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    nama_barang = models.CharField(max_length = 255)
    deskripsi = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add = True)
    kategori = models.ForeignKey(Kategori, on_delete=models.RESTRICT, to_field="jenis")
    available = models.BooleanField(default=False)