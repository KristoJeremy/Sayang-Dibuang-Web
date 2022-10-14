from django.urls import path
from barang_bekas.views import create_barang, get_all_barang_json, get_one_barang_json

app_name = 'barang_bekas'

urlpatterns = [
    # path('', view_name, name=''),
    path('upload/', create_barang, name="create_barang")
]