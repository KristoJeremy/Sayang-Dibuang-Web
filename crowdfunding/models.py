from django.db import models

# Create your models here.
class Crowdfund(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    received = models.IntegerField()  # number of items received by the user
    target = models.IntegerField()  # number of items needed by the user
    is_accomplished = models.BooleanField(
        default=False
    )  # is the target of the crowdfund is achieved?
