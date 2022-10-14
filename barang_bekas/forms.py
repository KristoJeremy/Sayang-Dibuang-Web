from django import forms
from barang_bekas.models import Barang, Lokasi, Kategori

class CreateBarangForm(forms.ModelForm):

    class Meta:
        model = Barang
        fields = ('judul', 'deskripsi', 'lokasi', 'kategori')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lokasi'].queryset = Lokasi.objects.none()
        self.fields['kategori'].queryset = Kategori.objects.none()