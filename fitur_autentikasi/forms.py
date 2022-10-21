from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from fitur_autentikasi.models import Profile

import re

class ProfileForm(forms.ModelForm):

    def clean_telephone(self):
        data = self.cleaned_data["telephone"]

        regex_for_phone_number = r"(0|\+{0,3}[0-9]{2})[0-9]{9,11}"

        if (re.match(regex_for_phone_number, data)):
            return data 

        raise forms.ValidationError("Phone number is not valid!")

    def clean_whatsapp(self):
        data = self.cleaned_data["whatsapp"]

        regex_for_phone_number = r"(0|\+{0,3}[0-9]{2})[0-9]{9,11}"

        if (re.match(regex_for_phone_number, data) or not data):
            return data 

        raise forms.ValidationError("Whatsapp is not valid!")

    class Meta:
        model = Profile
        fields = ('telephone', 'whatsapp', 'line')
    
    telephone = forms.CharField(label="telephone", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Start with 0/+XX/XX"}))
    whatsapp = forms.CharField(label="whatsapp", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Start with 0/+XX/XX"}), required=False)
    line = forms.CharField(label="line", widget=forms.TextInput(attrs={"class": "form-control"}), required=False)

class UserForm(UserCreationForm):

    def clean_email(self):
        """
        source: https://stackoverflow.com/questions/47816044/how-to-validate-for-unique-email-while-signing-up
        Returns the email if entered email is unique otherwise gives duplicate_email error.
        """
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exist')
        return email

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email',)

    username = forms.CharField(label="username", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(label="first_name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32)
    last_name=forms.CharField(label="last_name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32)
    email=forms.EmailField(label="email", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64)
    password1=forms.CharField(label="password1", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2=forms.CharField(label="password2", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))