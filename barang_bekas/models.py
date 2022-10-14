from ast import mod
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
# kalo pke ini nanti user pas upload bisa tinggal milih dari kategori yg dh ad gitu ato nambah baru,, tapi gmn WKKWK
# ato lokasi sm kategorinya udh diisi default dari kita 

class Lokasi (models.Model):
    nama = models.CharField(max_length = 255)

class Kategori (models.Model):
    jenis =  models.CharField(max_length = 255) 

class Barang (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foto = CloudinaryField("Image", overwrite=True, format="jpg")
    judul = models.CharField(max_length = 255)
    deskripsi = models.TextField()
    uploaded_at = models.DateField(auto_now_add = True)
    lokasi = models.ForeignKey(Lokasi, on_delete=models.RESTRICT)
    kategori = models.ForeignKey(Kategori, on_delete=models.RESTRICT)

# kalau mw pke combobox bisa baca di sini https://stackoverflow.com/questions/27081815/what-is-the-best-way-to-write-a-combo-box-in-django 
# https://codepolitan.com/blog/membuat-dropdown-bersyarat-dengan-django-5a71423f2af24