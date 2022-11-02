from django import forms
from django.forms import ModelForm
from leaderboard.models import Message

# Form untuk mendapatkan pesan dari user
class UploadMessage(ModelForm):
    random_message = forms.CharField()
    class Meta:
        model = Message
        fields = ['random_message']