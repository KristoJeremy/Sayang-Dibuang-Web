from django import forms
from django import forms
from fitur_autentikasi.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('telephone', 'whatsapp', 'line')