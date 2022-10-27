from django.urls import path
from . import views

app_name = "crowdfunding"

urlpatterns = [
    path("", views.show_crowdfundings, name="show_crowdfundings"),
    path("<int:id>/", views.show_crowdfunding_by_id, name="show_crowdfunding_by_id"),
    path("create/", views.create_crowdfund, name="create_crowdfund"),
    path("edit/<int:id>", views.edit_crowdfund, name="edit_crowdfund"),
    path("delete/<int:id>", views.delete_crowdfund, name="delete_crowdfund"),
    path("json/", views.show_crowdfundings_json, name="show_crowdfundings_json"),
    path(
        "json/<int:id>",
        views.show_crowdfundings_by_id_json,
        name="show_crowdfundings_by_json",
    ),
    path("get-user-by-id/<int:id>", views.get_user_by_id, name="get_user_by_id"),
]
