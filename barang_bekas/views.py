import re
from django.shortcuts import render
from barang_bekas.models import Barang
from django.shortcuts import HttpResponse, render, redirect
from django.core import serializers
from django.http.response import JsonResponse
from barang_bekas.forms import CreateBarangForm
from cloudinary.forms import cl_init_js_callbacks   

# Create your views here.
# 1. add barang 
def create_barang(request):
    # protect page
    if not request.user.is_authenticated:
        return redirect("/login/") 
    form = CreateBarangForm()

    if request.method=="POST":
        form = CreateBarangForm(request.POST, request.FILES)
        if form.is_valid():
            new_barang = form.save(commit=False)
            new_barang.user = request.user
            new_barang.save() 
        # user = request.user
        # judul = request.POST.get('judul')
        # deskripsi = request.POST.get('deskripsi')
        # lokasi = request.POST.get('lokasi')
        # kategori = request.POST.get('kategori')
        # item = Barang(user=user, judul=judul, deskripsi=deskripsi, lokasi=lokasi,  kategori=kategori)
        # item.save()
            return JsonResponse({
                "Message": "Item Berhasil Dibuat", 
            },status=201)

        return JsonResponse({
            "Message": "Item TIDAK Berhasil Dibuat", 
        },status=500)
    context = {'form':form}
    return render(request, 'upload.html', context)

# 2. get barang (public)
def get_all_barang_json(request):
    list_barang = Barang.objects.all()
    return HttpResponse(serializers.serialize("json", list_barang), content_type="application/json")

def get_one_barang_json(request, id):
    barang = Barang.objects.get(pk=id)
    return HttpResponse(serializers.serialize("json", barang), content_type="application/json")

# 3. edit barang
# 4. delete barang

# bikin modal buat add category & lokasii?? tapi gabisa edit/delete (masi mikir )
# 5. add kategori
# 6. add lokasi
