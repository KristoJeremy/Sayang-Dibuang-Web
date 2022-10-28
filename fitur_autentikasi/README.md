# Fitur Autentikasi
Fitur autentikasi bertujuan agar halaman atau fitur tertentu hanya dapat diakses ketika pengguna telah terdaftar dan login (terautentikasi).

***

## Dokumentasi
1. URL Mapping<br>
    - `https://sayang-dibuang.herokuapp.com/login` untuk mengakses halaman login
    - `http://sayang-dibuang.herokuapp.com/register` untuk mengakses halaman register
    - `https://sayang-dibuang.herokuapp.com/logout` untuk mengakses halaman logout
    - `https://sayang-dibuang.herokuapp.com/profile/<username>` untuk mengakses profil user

2. Restriksi akses halaman web tertentu<br>
Tambahkan potongan kode berikut pada fungsi views untuk merestriksi akses ke halaman web tertentu. Hal ini bertujuan agar pengguna yang ingin mengakses halaman tersebut harus mempunyai akun terlebih dahulu dan login ke situs web.
    ```python
    from django.contrib.auth.decorators import login_required

    @login_required(login_url='/login/')
    def fungsi_yang_ingin_direstriksi():
        pass
    ```
    > Tambahkan `@login_required(login_url='/login/')` pada fungsi views yang membutuhkan autentikasi pengguna. 

    > Decorator `login_required(login_url='/login/')` merupakan `Django Authorization` yang berfungsi untuk mengecek apakah pengguna telah terautentikasi
3. Button logout<br> 
Tambahkan baris kode berikut pada template yang dibuat sehingga pengguna dapat *logout*.
    ```html
    <button><a href="{% url 'fitur_autentikasi:logout' %}">Logout</a></button>
    ```
4. Pengaksesan field pada model Profile<br>
    ```python
    from fitur_autentikasi.models import Profile

    def my_view(request):
        user = Profile.objects.get(user=request.user)
        user_telephone = user.telephone
        user_whatsapp = user.whatsapp
        user_line = user.line
        user_poin = user.poin

        user_email = user.get_email()
        user_fullname = user.get_fullname()
        
        # Menambahkan poin keaktifan sebesar 10 kepada user
        user.add_poin(10)
    ```
    ```python
    # Alternatif
     def my_view(request):
        user = request.user
        user_telephone = user.profile.telephone
        user_whatsapp = user.profile.whatsapp
        user_line = user.profile.line
        user_poin = user.profile.poin

        user_email = user.profile.get_email() # alt: user.email
        user_fullname = user.profile.get_fullname()
        
        # Menambahkan poin keaktifan sebesar 15 kepada user
        user.profile.add_poin(15)
    ```
    > Untuk konsistensi, pilih salah satu metode pengaksesan field saja
5. Pengubahan field pada model Profile<br>

    ```python
    from fitur_autentikasi.models import Profile

    def my_view(request):
        user = Profile.objects.get(user=request.user)

        # Mengubah poin keaktifan user menjadi 0
        user.set_poin(0)
    ```
    > Untuk pengubahan field telephone, whatsapp, dan line dapat dilakukan dengan memanfaatkan `ProfileForm`. Hal ini dikarenakan `ProfileForm` memiliki validator untuk mengecek validitas masukkan user untuk telephone, whatsapp, dan line.

6. Mengakses halaman profil user<br>
Tambahkan baris kode berikut pada template yang dibuat sehingga pengguna dapat mengakses halaman profil.
    ```html
    <button><a href="{% url 'fitur_autentikasi:show_profile' username=<nama_user> %}">Profil</a></button>
    ```
    > Perhatikan bahwa `<nama_user>` harus diganti dengan username dari user yang telah terautentikasi. Oleh karena itu, jangan lupa untuk menyimpan `nama_user` pada variabel `context` pada fungsi `views.py` kalian.

    Contoh
    ```python
    # Pada views.py di aplikasi kalian
    def hello_world(request):
        context = {'user': request.user}
        return render(request, "test.html")
    ```
    ```html
    <!-- Pada test.html -->
    {% extends 'base.html' %}

    {% block meta %}
    <title>Test</title>
    {% endblock meta %}

    {% block content %}  
    <h1>Hello world</h1>
    <button><a href="{% url 'fitur_autentikasi:show_profile' username=user.username %}">Profil</a></button>

    {% endblock content %}
    ```

    ***

    ## Sumber referensi
    1. https://dev.to/earthcomfy/django-user-profile-3hik
    2. https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
    3. https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
