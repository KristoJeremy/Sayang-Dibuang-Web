from django.urls import path
from barang_bekas.views import create_barang, get_all_barang_json, get_one_barang_json, show_barang, show_barang_detail, edit_barang, create_kategori

app_name = 'barang_bekas'

urlpatterns = [
    # path('', view_name, name=''),
    path('', show_barang, name="show_barang"),
    path('all/', get_all_barang_json, name="get_all_barang_json"),
    path('<int:id>/', show_barang_detail, name="show_barang_detail"),
    path('<int:id>/edit/', edit_barang, name="edit_barang"),
    path('upload/', create_barang, name="create_barang"),
    path('add/kategori/', create_kategori, name="create_kategori")
]