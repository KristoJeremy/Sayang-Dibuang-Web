from django.urls import path
from barang_bekas.views import *

app_name = 'barang_bekas'

urlpatterns = [
    # path('', view_name, name=''),
    path('', show_barang, name="show_barang"),
    path('all/', get_all_barang_json, name="get_all_barang_json"),
    path('json/<int:id>', get_one_barang_json, name="get_one_barang_json"),
    path('<int:id>/', show_barang_detail, name="show_barang_detail"),
    path('<int:id>/edit/', edit_barang, name="edit_barang"),
    path('<int:id>/delete/', delete_barang, name="delete_barang"),
    path('upload/', create_barang, name="create_barang"),
    path('upload/ajax/', create_barang_ajax, name="create_barang"),
    path('add/kategori/', create_kategori, name="create_kategori"),
    path('kategori/', get_kategori_ajax, name="get_kategori_ajax"),
    path('add/lokasi/', create_lokasi, name="create_lokasi"),
    path('lokasi/', get_lokasi_ajax, name="get_lokasi_ajax"),
]