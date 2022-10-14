from django import forms
from barang_bekas.models import Barang, Lokasi, Kategori

class CreateBarangForm(forms.ModelForm):
    # Lokasi = forms.ModelChoiceField(queryset=Lokasi.objects.all())
    class Meta:
        model = Barang
        fields = ('judul', 'deskripsi', 'lokasi', 'kategori')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lokasi'].queryset = Lokasi.objects.all()
        self.fields['kategori'].queryset = Kategori.objects.all()