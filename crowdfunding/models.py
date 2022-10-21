from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Crowdfund(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    received = models.IntegerField()  # number of items received by the user
    target = models.IntegerField()  # number of items needed by the user
    is_accomplished = models.BooleanField(default=False)
