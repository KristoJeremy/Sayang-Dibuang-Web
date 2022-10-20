from django import forms
from fitur_autentikasi.models import Profile

import re

class ProfileForm(forms.ModelForm):

    def clean_telephone(self):
        data = self.cleaned_data["telephone"]

        regex_for_phone_number = r"(0|\+{0,2}[0-9]{2})[0-9]{9,11}"

        if (re.match(regex_for_phone_number, data)):
            return data 

        raise forms.ValidationError("Phone number is not valid!")

    def clean_whatsapp(self):
        data = self.cleaned_data["whatsapp"]

        regex_for_phone_number = r"(0|\+{0,2}[0-9]{2})[0-9]{9,11}"

        if (re.match(regex_for_phone_number, data)):
            return data 

        raise forms.ValidationError("Whatsapp is not valid!")

    class Meta:
        model = Profile
        fields = ('telephone', 'whatsapp', 'line')
    
    telephone = forms.CharField(label="telephone", widget=forms.TextInput(attrs={"placeholder": "Start with 0/+XX/XX"}))
    whatsapp = forms.CharField(label="whatsapp", widget=forms.TextInput(attrs={"placeholder": "Start with 0/+XX/XX"}))
    line = forms.CharField(label="line")

    