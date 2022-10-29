from django import forms
from information.models import *

class CreateReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('judul', 'deskripsi')