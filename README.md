# Kelompok PBP D10: Sayang-Dibuang
[![Deploy](https://github.com/D10-PBP/Proyek-Tengah-Semester/actions/workflows/dpl.yml/badge.svg)](https://github.com/D10-PBP/Proyek-Tengah-Semester/actions/workflows/dpl.yml)

## 📌 Nama Anggota 📌
1. Lyzander Marciano Andrylie - 2106750755
2. Gibrano Fabien Derenz - 2106750622
3. Khansa Jovita - 2106651686
4. Kristo Jeremy Thady Tobing - 2106633310
5. Pikatan Arya Bramajati - 2106630031
6. Catherine Angel Robin - 2106705392

## ✨ Tautan Aplikasi Heroku ✨
- Nama aplikasi kami: `Sayang-Dibuang`
- Link: https://sayang-dibuang.up.railway.app/ (telah migrasi dari Heroku)

## 📜 Cerita Aplikasi dan Manfaat 📜
### Cerita
Aplikasi `Sayang-Dibuang` memungkinkan _user_ untuk berbagi makanan dan/atau barang layak berlebih kepada pengguna lain yang membutuhkan secara gratis. Aplikasi ini memiliki fitur _request_ sebagai pendukung _user_ yang membutuhkan suatu barang. Dengan kehadiran `Sayang-Dibuang`, makanan dan barang yang terbuang sia-sia dapat diminimalisasi.

### Manfaat
    1. Mengurangi sampah makanan dan/atau barang tidak terpakai;
    2. Membantu mengurangi dampak buruk pada ozon dan pemanasan global (makanan bekas yang dibiarkan menyebabkan terbentuknya gas metana);
    3. Membantu sesama manusia dalam memenuhi kebutuhannya.

## 💻 Daftar modul yang akan diimplementasikan 💻
1. **Authentication (Register, Login, Logout)**<br>
    Fitur ini diperlukan untuk autentikasi user yang hendak menggunakan aplikasi ini. User akan memiliki atribut:
    * Nama
    * Email
    * Password
    * Contact info (no. telp, whatsapp, line)
    * Poin keaktifan di aplikasi (akan dimanfaatkan di fitur Leaderboard)
    
2. **Information**<br>
    Pada bagian ini, akan disajikan landing page, about us page, dan frequently asked questions page sebagai pengantar publik kepada aplikasi kami.

    Untuk membuat fitur ini, tidak diperlukan model.

3. **Beranda Barang Bekas**<br>
     Fitur ini memampukan user yang sudah register dan login akun untuk melihat semua barang yang sedang diedar di aplikasi.

    Selain itu, user juga dapat mempost barang bekas yang ia miliki. Hasil post ini dapat dilihat oleh user lain di Dashboard Barang Bekas.

    Untuk mengimplementasikan fitur ini, diperlukan suatu model Barang yang memuat atribut berikut:
    * Foto
    * Judul
    * Deskripsi
    * Lokasi
    * Kategori

4. **Request Barang Bekas**<br>
    Pada fitur ini, user yang sudah register dan login akun bisa menyampaikan keinginannya mengenai suatu barang bekas, sehingga bisa dilihat oleh user lain. User yang mempunyai barang tersebut dapat menghubungi user yang me-requestnya.

    Untuk mengimplementasikan fitur ini, dibutuhkan model RequestBarang dengan atribut:
    * User (yang mempost request barang bekas)
    * Nama barang
    * Deskripsi
    * Kategori

5. **_Crowdfunding_**<br> 
    Pada fitur ini, user yang sudah register dan login akun bisa membuat suatu kampanye mengenai target kebutuhannya dengan barang bekas (misalnya membutuhkan 20 karton telur untuk proyek kelas seni rupa). User yang berkenan menyumbangkan barang bekasnya bisa menghubungi user yang membuat kampanye tersebut untuk diberikan barang.

    Jika sudah terjadi progres kampanye, maka user yang membuat kampanye di awal bisa update status kampanye (misalnya telah menerima 20% dari target jumlah barang bekas, 40% dari target jumlah barang bekas, dan seterusnya).

    Untuk mengimplementasikan fitur ini, diperlukan model Crowdfund yang memuat atribut:
    * User (yang mempost crowdfund)
    * Judul
    * Deskripsi (penjelasan kebutuhan user yang mempost crowdfund ini)
    * Waktu dipost
    * Target (jumlah barang bekas yang diharapkan)
    * Penerimaan (jumlah barang bekas yang sudah diterima)
    * Sudah tercapai (apakah target crowdfund sudah tercapai)

6. **Leaderboard, badges (gamifikasi)**<br>
    Leaderboard berisikan urutan peringkat user dari achievement point tertinggi. Setiap kali user berbagi barang atau menerima barang, maka poin akan terus bertambah. Setiap kali poin menyentuh tingkat tertentu, maka user akan mendapatkan suatu badge.

    Untuk membuat fitur ini, tidak diperlukan model.

## Roles pengguna pada aplikasi `Sayang-Dibuang`<br>
    1. Admin
    2. Public (Orang-orang yang mengakses aplikasi, tetapi belum membuat akun. Public hanya dapat mengakses fitur Information saja)
    3. User (Orang-orang yang sudah login dan dapat mengakses semua fitur pada aplikasi sayang-dibuang)
