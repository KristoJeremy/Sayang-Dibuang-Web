from email.policy import default
from django.db import models
from tinymce.models import HTMLField
from fitur_autentikasi.models import Profile

# Create your models here.
class Crowdfund(models.Model):
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True, to_field="user"
    )
    title = models.CharField(max_length=255)
    description = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    received = models.IntegerField(default=0)  # number of items received by the user
    target = models.IntegerField()  # number of items needed by the user
    is_accomplished = models.BooleanField(default=False)
    helpers = models.ManyToManyField(Profile, related_name="profiles")
