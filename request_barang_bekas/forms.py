from django import forms
from request_barang_bekas.models import Request
from barang_bekas.models import Kategori

class CreateRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ("nama_barang", "deskripsi", "kategori", "available")
        widgets = {
          "deskripsi": forms.Textarea(attrs={"rows":4, "cols":25}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["kategori"].queryset = Kategori.objects.all() 
        self.fields["available"].required = False