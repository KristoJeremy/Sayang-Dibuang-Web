from django import forms
from django.forms import ModelForm
from leaderboard.models import Message

class UploadMessage(ModelForm):
    random_message = forms.CharField()
    class Meta:
        model = Message
        fields = ['random_message']