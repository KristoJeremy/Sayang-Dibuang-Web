from django.urls import path
from . import views

app_name = "crowdfunding"

urlpatterns = [
    path("", views.show_crowdfundings, name="show_crowdfundings"),
    path("<int:id>/", views.show_crowdfunding_by_id, name="show_crowdfunding_by_id"),
    path("create/", views.create_crowdfund, name="create_crowdfund"),
]
