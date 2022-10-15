from django.urls import path
from . import views

app_name = "crowdfunding"

urlpatterns = [path("", views.show_crowdfundings, name="show_crowdfundings")]
