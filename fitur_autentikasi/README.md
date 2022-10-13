# Fitur Autentikasi
Fitur autentikasi bertujuan agar halaman atau fitur tertentu hanya dapat diakses ketika pengguna telah terdaftar dan login (terautentikasi).

***

## Note
1. Tambahkan `from django.contrib.auth.decorators import login_required` dan `@login_required(login_url='/login/')` pada fungsi views yang membutuhkan autentikasi pengguna.
2. Tambahkan `<button><a href="{% url 'fitur_autentikasi:logout' %}">Logout</a></button>` pada template yang dibuat sehingga pengguna dapat *logout*.