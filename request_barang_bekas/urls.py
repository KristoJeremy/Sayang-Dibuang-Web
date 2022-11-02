from django.urls import path
from request_barang_bekas.views import show_requests, create_request, show_all_requests_json, show_request_details, edit_request, delete_request

app_name = "request_barang_bekas"

urlpatterns = [
    path("", show_requests, name="show_requests"),
    path("upload/", create_request, name="create_request"),
    path("all/", show_all_requests_json, name="creashow_all_requests_jsonte_request"),
    path("<int:id>/", show_request_details, name="show_request_details"),
    path("<int:id>/edit/", edit_request, name="edit_request"),
    path("<int:id>/delete/", delete_request, name="delete_request"),
]