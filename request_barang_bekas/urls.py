from django.urls import path
from request_barang_bekas.views import *

app_name = "request_barang_bekas"

urlpatterns = [
    path('', show_request, name="show_requests"),
    path('all/', get_all_request_json, name="get_all_request_json"),
    path('all/mobile/', get_all_request_mobile, name="get_all_request_mobile"),
    path('json/<int:id>', get_one_request_json, name="get_one_request_json"),
    path('owner/<int:id>/', get_owner_request, name="get_owner_request"),
    path('<int:id>/', show_request_detail, name="show_request_detail"),
    path('<int:id>/edit/', edit_request, name="edit_request"),
    path('<int:id>/edit/ajax/', edit_request_ajax, name="edit_request_ajax"),
    path('<int:id>/delete/', delete_request, name="delete_request"),
    path('<int:id>/delete/mobile/', delete_request_mobile, name="delete_request_mobile"),
    path('upload/', create_request, name="create_request"),
    path('upload/ajax/', create_request_ajax, name="create_request_ajax"),
]