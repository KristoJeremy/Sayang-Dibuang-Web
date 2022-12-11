from django.contrib import admin
from barang_bekas.models import Barang, Kategori, Lokasi, BarangMobile

# Register your models here.
admin.site.register(Barang)
admin.site.register(Kategori)
admin.site.register(Lokasi)
admin.site.register(BarangMobile)
