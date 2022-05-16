# Pertemuan 10: Akses Ke Basis Data CockroachDB menggunakan Psycopg2 dan menggunakan SQLAlchemy
## Bangun Aplikasi Python dengan CockroachDB dan psycopg2

Tutorial ini akan menunjukkan kepada kita bagaimana membangun aplikasi Python sederhana dengan CockroachDB dan driver psycopg2
### Langkah 1. Mulai CockroachDB
Buat cluster gratis
1. jika kita belum melakukannya, daftar akun CockroachDB Cloud
2. Masuk ke akun Cloud CockroachDB Anda
3. Pada halaman Cluster , klik Buat Cluster
4. Pada halaman Buat kluster Anda , pilih Tanpa Server
5. Klik Buat kluster

Buat pengguna SQL
1. Masukkan nama pengguna di bidang pengguna SQL atau gunakan yang disediakan 2. secara default
3. Klik Buat & simpan kata sandi
4. Salin kata sandi yang dihasilkan dan simpan di lokasi yang aman
5. Klik Berikutnya

Dapatkan sertifikat root
1. Pilih String koneksi umum dari dropdown Pilih opsi
2. Buka terminal baru di komputer lokal Anda, dan jalankan perintah unduhan CA Cert yang disediakan di bagian Unduh CA Cert . Driver klien yang digunakan dalam tutorial ini memerlukan sertifikat ini untuk terhubung ke CockroachDB Cloud

Dapatkan string koneksi
Buka bagian General connection string , lalu salin connection string yang disediakan dan simpan di lokasi yang aman.

### Langkah 2. Dapatkan kode sampel
Kloning repo GitHub kode sampel:
``git clone https://github.com/cockroachlabs/hello-world-python-psycopg2``
Kode sampel di `example.py` melakukan hal berikut:
- Membuat accountstabel dan menyisipkan beberapa baris
- Mentransfer dana antara dua akun dalam suatu transaksi
- Hapus akun dari tabel sebelum keluar sehingga Anda dapat menjalankan kembali kode contoh

### Langkah 4. Jalankan kode
1. Setel `DATABASE_URLvariabel` lingkungan ke string koneksi ke cluster CockroachDB Cloud Anda:
`export DATABASE_URL="{connection-string}"`
Di mana `{connection-string}string` koneksi yang Anda peroleh dari CockroachDB Cloud Console.

Aplikasi menggunakan string koneksi yang disimpan ke `DATABASE_URLvariabel` lingkungan untuk terhubung ke cluster Anda dan mengeksekusi kode.
2. jalankan kode
 ```cd hello-world-python-psycopg2```
```python example.py```

Output harus menunjukkan saldo akun sebelum dan sesudah transfer dana:
```Balances at Fri Oct 30 18:27:00 2020:
(1, 1000)
(2, 250)
Balances at Fri Oct 30 18:27:00 2020:
(1, 900)
(2, 350)```

