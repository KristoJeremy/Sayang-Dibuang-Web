from django import forms
from .models import Crowdfund


class CrowdfundForm(forms.ModelForm):
    class Meta:
        model = Crowdfund
        fields = ["title", "description", "received", "target"]
