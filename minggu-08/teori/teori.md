## 1. antarmuka sistem oprasi
Modul os menyediakan puluhan fungsi untuk berinteraksi dengan sistem operasi. Fungsi bawaan `dir()` dan `help()` berguna sebagai alat bantu interaktif untuk bekerja dengan modul besar seperti os. modul shutil menyediakan antarmuka level yang lebih tinggi yang lebih mudah digunakan.
## 2. berkas wildcard
merupakan sebuah modul glob yang berfungsi untuk membuat daftar berkas wildcard pada direktori.
## 3. baris perintah berargumen
argumen-argumen ini disimpan dalam atribut argv dari modul sys sebagai daftar. Modul argparse menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah. Modul `sys` juga memiliki atribut untuk `stdin`, `stdout`, dan `stderr`. Yang terakhir berguna untuk mengirimkan peringatan dan pesan kesalahan untuk membuatnya terlihat bahkan ketika stdout telah dialihkan. 
## 4. pencocokan pola string
Modul `re` menyediakan alat ekspresi reguler untuk pemrosesan `string` lanjutan. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan. Ketika hanya kemampuan sederhana yang diperlukan, metode `string` lebih disukai karena lebih mudah dibaca dan dilakukan debug.
## 5. matematika
Modul math memberikan akses ke fungsi-fungsi pustaka C yang mendasari untuk matematika angka pecahan floating point. Modul random menyediakan alat untuk membuat pilihan acak. Modul statistics menghitung sifat statistik dasar (rata-rata, median, varian, dll.) dari data numerik.
## 6. kompresi data
Format pengarsipan dan kompresi data umum didukung langsung oleh modul-modul yang ada antara lain: zlib, gzip, bz2, lzma, zipfile dan tarfile.
## 7. tanggal dan waktu
Modul datetime menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks. Sementara aritmatika tanggal dan waktu didukung, fokus implementasi adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran. 
## 8. pengukuran kinerja
Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari berbagai pendekatan untuk masalah yang sama. Berbeda dengan granularity tingkat halus timeit, modul profile dan pstats menyediakan alat untuk mengidentifikasi bagian kritis waktu dalam blok kode yang lebih besar.  
## 9. pemformatan output
 Modul reprlib menyediakan versi `repr()` yang disesuaikan untuk tampilan yang disingkat dari wadah containers yang besar atau sangat bersarang. Modul pprint menawarkan kontrol yang lebih canggih atas pencetakan objek bawaan dan yang ditentukan pengguna dengan cara yang dapat dibaca oleh interpreter. Ketika hasilnya lebih dari satu baris, `"pretty printer"` menambahkan jeda baris dan indentasi untuk lebih jelas mengungkapkan struktur data. Modul `textwrap` memformat paragraf teks agar sesuai dengan lebar layar yang diberikan. Modul locale mengakses basis data format data kultur khusus. Atribut pengelompokan fungsi format lokal locale menyediakan cara langsung memformat angka dengan pemisah grup.

## 10. templeting
Modul `string` menyertakan kelas serbaguna Template dengan sintaks yang disederhanakan yang cocok untuk diedit oleh pengguna. Format ini menggunakan nama penampung yang dibentuk oleh `$` dengan pengidentifikasi Python yang valid (karakter alfanumerik dan garis bawah). Metode substitute() memunculkan `KeyError` saat placeholder tidak disertakan dalam dictionary atau argumen kata kunci keyword argument.
## 11. pencatatan
Modul logging menawarkan sistem pencatatan logging yang lengkap dan fleksibel. Paling sederhana, catatan log pesan dikirim ke berkas atau ke sys.stderr. Secara bawaan, pesan informasi dan debugging ditutupi suppressed dan keluaran dikirim ke standar kesalahan. Sistem pencatatan dapat dikonfigurasikan secara langsung dari Python atau dapat dimuat dari berkas konfigurasi yang dapat diedit pengguna untuk pencatatan yang disesuaikan tanpa mengubah aplikasi. 
## 12. refrensi yang lemah
Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan garbage collection untuk menghilangkan siklus). Pendekatan ini berfungsi dengan baik untuk sebagian besar aplikasi tetapi kadang-kadang ada kebutuhan untuk melacak objek hanya selama mereka digunakan oleh sesuatu yang lain
## 13. alat untuk bekerja dengan daftar list
Modul array menyediakan objek `array()` yang seperti daftar list dimana hanya menyimpan data homogen dan menyimpannya dengan lebih kompak. Modul collections menyediakan objek `deque()` yang seperti daftar list dengan tambahan yang lebih cepat dan muncul dari sisi kiri tetapi pencarian yang lebih lambat di tengah. Selain implementasi daftar list alternatif, di pustaka juga menawarkan alat-alat lain seperti modul bisect dengan fungsi untuk memanipulasi daftar list yang diurutkan. Modul `heapq` menyediakan fungsi untuk mengimplementasikan heaps berdasarkan daftar list reguler.
## 14. Aritmatika Pecahan Floating Point Desimal
Modul decimal menawarkan Decimal tipe data untuk aritmatika pecahan desimal.

- aplikasi keuangan dan penggunaan lainnya yang membutuhkan representasi desimal yang tepat.
- kontrol atas presisi.
- kontrol atas pembulatan untuk memenuhi persyaratan sah legal atau peraturan,
- pelacakan tempat desimal yang signifikan, atau
- aplikasi tempat pengguna mengharapkan hasil agar sesuai dengan perhitungan yang dilakukan dengan tangan.
