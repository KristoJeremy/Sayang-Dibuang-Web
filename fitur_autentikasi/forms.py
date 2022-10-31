from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from fitur_autentikasi.models import Profile

import re

class ProfileForm(forms.ModelForm):

    def clean_telephone(self):
        data = self.cleaned_data["telephone"]

        regex_for_phone_number = r"(0|\+{0,1}[0-9]{1,3})[0-9]{9,11}"

        if (re.match(regex_for_phone_number, data)):
            return data 

        raise forms.ValidationError("Nomor telepon tidak valid!")

    def clean_whatsapp(self):
        data = self.cleaned_data["whatsapp"]

        regex_for_phone_number = r"(0|\+{0,1}[0-9]{1,3})[0-9]{9,11}"

        if (re.match(regex_for_phone_number, data) or not data):
            return data 

        raise forms.ValidationError("Nomor Whatsapp tidak valid!")

    class Meta:
        model = Profile
        fields = ('telephone', 'whatsapp', 'line')
    
    telephone = forms.CharField(label="Nomor telepon", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "+62/62/08xxx"}))
    whatsapp = forms.CharField(label="Nomor Whatsapp", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "+62/62/08xxx"}), required=False)
    line = forms.CharField(label="ID Line", widget=forms.TextInput(attrs={"class": "form-control"}), required=False)

class UserForm(UserCreationForm):

    def clean_email(self):
        """
        source: https://stackoverflow.com/questions/47816044/how-to-validate-for-unique-email-while-signing-up
        Returns the email if entered email is unique otherwise gives duplicate_email error.
        """
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email sudah terdaftar')
        return email

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email',)

    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete":"new-password"}))
    password2 = forms.CharField(label="Konfirmasi password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Kembali', "autocomplete":"new-password"}))
    first_name = forms.CharField(label="Nama depan", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Depan'}), max_length=50)
    last_name = forms.CharField(label="Nama belakang", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Belakang'}), max_length=50, required=False)
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex: sayangdibuang@gmail.com'}), max_length=64)

class UserUpdateForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name')
    
    first_name = forms.CharField(label="Nama depan", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Depan'}), max_length=50)
    last_name = forms.CharField(label="Nama belakang", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Belakang'}), max_length=50, required=False)