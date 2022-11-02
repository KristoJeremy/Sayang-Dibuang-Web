from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    line = models.CharField(max_length=100)
    poin = models.IntegerField(default=0)
    
    def set_poin(self, poin):
        self.poin = poin
        self.save()

    def add_poin(self, poin):
        '''
        Fungsi untuk menambahkan poin keaktifan
        '''
        self.poin += poin
        self.save()

    def get_fullname(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    def get_email(self):
        return self.user.email