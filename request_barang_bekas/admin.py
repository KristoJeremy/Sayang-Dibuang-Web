from django.contrib import admin
from request_barang_bekas.models import Request, RequestMobile
from barang_bekas.models import Kategori

admin.site.register(Request)
admin.site.register(Kategori)
admin.site.register(RequestMobile)