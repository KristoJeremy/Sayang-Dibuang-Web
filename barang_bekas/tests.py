import datetime
from django.test import TestCase
from django.urls import resolve, reverse
from .models import Lokasi, Barang, Kategori

from .views import show_barang, show_barang_detail, create_barang, create_kategori, create_lokasi, delete_barang, edit_barang, get_all_barang_json, get_one_barang_json
from fitur_autentikasi.models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class BarangTest(TestCase):


    def test_show_barang_url(self):
        url = reverse("barang_bekas:show_barang")
        self.assertEquals(resolve(url).func, show_barang)
        

    def test_show_barang_detail_url(self):
        url = reverse("barang_bekas:show_barang_detail", args = [1])
        self.assertEquals(resolve(url).func, show_barang_detail)

    def test_create_barang_url(self):
        url = reverse("barang_bekas:create_barang")
        self.assertEquals(resolve(url).func, create_barang)

    def test_delete_barang_url(self):
        url = reverse("barang_bekas:delete_barang", args = [1])
        self.assertEquals(resolve(url).func, delete_barang)

    def test_get_all_barang_json_url(self):
        url = reverse("barang_bekas:get_all_barang_json")
        self.assertEquals(resolve(url).func, get_all_barang_json)
    
    def test_get_one_barang_json_url(self):
        url = reverse("barang_bekas:get_one_barang_json", args = [1])
        self.assertEquals(resolve(url).func, get_one_barang_json)
    
    def test_get_create_lokasi_url(self):
        url = reverse("barang_bekas:create_lokasi")
        self.assertEquals(resolve(url).func, create_lokasi)
    
    def test_get_create_barang_url(self):
        url = reverse("barang_bekas:create_kategori")
        self.assertEquals(resolve(url).func, create_kategori)
    
    def test_get_edit_barang_url(self):
        url = reverse("barang_bekas:edit_barang", args = [1])
        self.assertEquals(resolve(url).func, edit_barang)


    def test_model_lokasi(self):
        lokasi = Lokasi.objects.create(
            nama = "Jakarta",
        )
        self.assertEqual(Lokasi.objects.get(nama = lokasi.nama), lokasi)
        self.assertTrue(isinstance(lokasi, Lokasi))

    def test_model_kategori(self):
        kategori = Kategori.objects.create(
            jenis = "Plastik",
        )
        self.assertEqual(Kategori.objects.get(jenis = kategori.jenis), kategori)
        self.assertTrue(isinstance(kategori, Kategori))

    # def test_model_barang(self):
    #     user = User.objects.create(
    #         username = "Test11111",
    #         password = "pass1234",
    #     )

    #     profile = Profile.objects.create(
    #         user = user,
    #         telephone = '081234567789',
    #         whatsapp = '081234567789',
    #         line = 'line.peserta',
    #     )

    #     lokasi = Lokasi.objects.create(
    #         nama="jakarta"
    #     )

    #     kategori = Kategori.objects.create(
    #         jenis="plastik"
    #     )

    #     barang = Barang.objects.create(
    #         user = user,
    #         profile = profile,
    #         foto = '',
    #         judul = 'Judul test',
    #         deskripsi = 'Deskripsi Barang',
    #         uploaded_at = '2022-10-01 00:00:00',
    #         lokasi = lokasi,
    #         kategori = kategori,
    #         available = False,
    #     )
      

    #     self.assertEqual(Barang.objects.get(judul = barang.judul), barang)
    #     self.assertEqual(isinstance(barang, Barang))