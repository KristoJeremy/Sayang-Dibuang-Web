from django import forms
from .models import Crowdfund
from django.core.exceptions import ValidationError


class CrowdfundForm(forms.ModelForm):
    class Meta:
        model = Crowdfund
        fields = ["title", "description", "received", "target"]
        labels = {
            "title": "Judul",
            "description": "Deskripsi Kebutuhan",
            "received": "Jumlah yang Telah Diterima",
            "target": "Jumlah yang Dibutuhkan",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs[
                "class"
            ] = "form-control mb-4 border-0 py-2 text-secondary"

    def clean_target(self):
        received = self.cleaned_data["received"]
        target = self.cleaned_data["target"]
        if target == 0:
            raise ValidationError("Jumlah yang diinginkan harus lebih dari 0!")
        if target < received:
            raise ValidationError(
                "Jumlah yang dibutuhkan harus lebih kecil atau sama dengan jumlah yang sudah diterima!"
            )
        if received < 0:
            raise ValidationError(
                "Jumlah yang sudah diterima tidak boleh bernilai negatif!"
            )
        return target
