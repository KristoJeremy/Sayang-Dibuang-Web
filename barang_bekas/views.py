
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from barang_bekas.models import Barang
from django.shortcuts import HttpResponse, render, redirect
from django.core import serializers
from django.http.response import JsonResponse
from barang_bekas.forms import CreateBarangForm
import cloudinary
from barang_bekas.models import Barang, Kategori, Lokasi, BarangMobile
from fitur_autentikasi.models import Profile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
# 1. add barang 
@login_required(login_url='/login/')
def create_barang(request):
    form = CreateBarangForm()

    if request.method=="POST":
        form = CreateBarangForm(request.POST, request.FILES)
        if form.is_valid():
            new_barang = form.save(commit=False)
            new_barang.user = request.user
            new_barang.profile = Profile.objects.get(user=request.user)
            new_barang.save() 
           
            return redirect('barang_bekas:show_barang')

        return JsonResponse({
            "Message": "Item TIDAK Berhasil Dibuat", 
        },status=500)
    context = {'form':form}
    return render(request, 'upload.html', context)

def create_barang_ajax(request):
    if request.method == "POST":
        body = request.POST
        username = request["username"]
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        # foto = request.FILES["image"]
        foto = body["foto"]
        judul = body["judul"]
        deskripsi = body["deskripsi"]
        lokasi = body["lokasi"]
        kategori = body["kategori"]
        item = BarangMobile(profile=profile, foto=foto, judul=judul, deskripsi=deskripsi, uploaded_at=datetime.datetime.now(), lokasi=lokasi, kategori=kategori, available=False)
        item.save()
        
        return HttpResponse(serializers.serialize('json', item),status=200)

# 2. get barang
def show_barang(request):
    context = {}
    return render(request, 'barang-bekas.html', context)

def show_barang_detail(request, id):
    barang = Barang.objects.select_related('profile').select_related('user').get(id=id)
    user = request.user 

    context = {
        'barang':barang,
        'user':user
    }
    return render(request, 'barang-details.html', context)

def get_all_barang_json(request):
    list_barang = Barang.objects.all().order_by('-uploaded_at')
    query = request.GET.get('search')
    if query != '':
        list_barang = Barang.objects.filter(judul__icontains=query).order_by('-uploaded_at')

    return HttpResponse(serializers.serialize('json', list_barang)) 

def get_all_barang_mobile(request):
    list_barang = BarangMobile.objects.all().order_by('-uploaded_at')
    query = request.GET.get('search')
    if query != '':
        list_barang = BarangMobile.objects.filter(judul__icontains=query).order_by('-uploaded_at')

    return HttpResponse(serializers.serialize('json', list_barang)) 


def get_one_barang_json(request, id):
    barang = Barang.objects.get(pk=id)
    return HttpResponse(serializers.serialize("json", barang), content_type="application/json")

# 3. edit barang (ref: https://www.geeksforgeeks.org/update-view-function-based-views-django/)
@login_required(login_url='/login/')
def edit_barang(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Barang, id = id, user=request.user)

    form = CreateBarangForm(request.POST or None, request.FILES or None, instance=obj)
    
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/barang/"+str(id))
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "barang-edit.html", context)

# 4. delete barang
def delete_barang(request, id):
    barang = Barang.objects.get(user=request.user, id=id)
    barang.delete()
    return HttpResponseRedirect(reverse("barang_bekas:show_barang"))


# bikin modal buat add category & lokasii?? tapi gabisa edit/delete (masi mikir )
# 5. add kategori
def create_kategori(request):
    if request.method=="POST":
        jenis = request.POST.get('jenis').capitalize()
        item = Kategori(jenis=jenis)
        item.save()
        response = {
            "pk":item.pk,
            "jenis": item.jenis
        }
        return JsonResponse(response,status=200)
        

def get_kategori_ajax(request):
    list_kategori = Kategori.objects.all()
    return HttpResponse(serializers.serialize('json', list_kategori)) 


# 6. add lokasi
def create_lokasi(request):
    if request.method=="POST":
        nama = request.POST.get('nama').capitalize()
        item = Lokasi(nama=nama)
        item.save()
        response = {
            "pk":item.pk,
            "nama": item.nama
        }
        return JsonResponse(response,status=200)

def get_lokasi_ajax(request):
    list_lokasi = Lokasi.objects.all()
    return HttpResponse(serializers.serialize('json', list_lokasi)) 
    