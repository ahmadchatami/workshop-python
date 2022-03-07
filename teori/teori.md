##6. modul
Jika kita keluar dari Python interpreter lalu masuk ke interpreter lagi, maka semua definisi (fungsi dan variabel) yang sudah kita buat akan hilang. jika kita ingin membuat program yang panjang, lebih baik kita menggunakan text editor untuk menyiapkan input untuk interpreter lalu kita jalankan dengan file tersebut sebagai input. penulisan program yang semakin panjang, kita bisa memisahnya menjadi beberapa file supaya maintenance nya lebih mudah. Kita mungkin juga ingin menggunakan fungsi yang telah kita tulis di beberapa program tanpa menyalin definisinya ke dalam setiap program.

python juga memiliki fitur pendukung untuk meletakan definisi di dalam sebuah file dan menggunakannya di dalam script atau instance interaktif milik interpreter.
Modul adalah sebuah file yang berisi definisi dan statement Python. Nama file adalah nama modul dengan penambahan suffix `.py` Di dalam sebuah modul, nama modul (string) tersedia sebagai value dari variabel global __name__. Sebagai contoh, gunakan text editor untuk membuat file bernama `fibo.py` di sebuah direktori.

##6.1 Modul lanjutan
Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Setiap modul memiliki tabel simbol pribadinya sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul.

Dan juga modul dapat mengimport modul lain. Tetapi tidak diharus untuk menempatkan semua pernyataan import di awal modul.
contoh pernyataan `inport` yang mengimport nama dari modul langsung ke tabel simbol modul pengimpor :
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

Dalam pernyataan di atas tidak memperkenalkan nama modul dari mana import diambil dalam tabel simbol lokal.


terdapat juga contoh untuk mengimpor seluruh nama yang didefinisikan olah modul:
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

##6.1.1 menjalankan modul sebagai script
Saat Anda menjalankan modul Python python `fibo.py <arguments>`, kode dalam modul akan dieksekusi.

jika Anda mengimpornya, tetapi dengan kode dalam modul akan dieksekusi, sama seperti jika Anda mengimpornya, tetapi dengan `__name__set ke "main"`.

##6.1.2 Modul Jalur Pencarian


Ketika sebuah modul bernama `spam` diimport, interpreter pertama-tama akan mencari modul bawaan dengan nama itu. Jika tidak ditemukan, maka kemudian akan mencari berkas bernama spam.py dalam daftar directory yang diberikan oleh variabel `sys.path.sys.path` yang diinisialisasi dari lokasi ini:

- Directory yang berisi script masukan (atau direktori saat ini ketika tidak ada file ditentukan).
- PYTHONPATH (daftar nama direktori, dengan sintaksis yang sama dengan variabel shell PATH).
- Default yang bergantung pada instalasi (berdasarkan konvensi termasuk site-packagesdirektori, ditangani oleh sitemodul).

Setelah inisialisasi, program Python dapat memodifikasi `data :sys.path`. Directory yang berisi script yang dijalankan dan ditempatkan di awal jalur pencarian, di depan jalur pustaka standar.

##6.1.3 File Python yang Dikompilasi
Untuk mempercepat memuat modul, Python menyimpan cache versi terkompilasi dari setiap modul di directory `__pycache__` dengan nama `module. version.pyc`, di mana versi menyandikan format berkas terkompilasi; umumnya berisi nomor versi Python. Misalnya, dalam rilis CPython 3.3 versi yang dikompilasi dari `spam.py` akan di-cache sebagai `__pycache__/spam.cpython-33`.pyc. Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis yang beragam dan versi Python yang berbeda.

Python memeriksa tanggal modifikasi sumber terhadap versi yang dikompilasi untuk melihat apakah itu kedaluwarsa dan perlu dikombinasi ulang. Hal tersebut adalah proses yang sepenuhnya otomatis. selain itu juga modul yang dikombinasi adalah platform-independen, sehingga perpustakaan yang sama dapat dibagi di antara sistem dengan arsitektur yang berbeda.

Di sisi lain Python tidak memeriksa cache dalam dua keadaan. Pertama, selalu mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang dimuat langsung dari baris perintah. Kedua, itu tidak memeriksa cache jika tidak ada modul sumber. Untuk mendukung distribusi non-sumber (dikompilasi saja), modul yang dikompilasi harus ada di directory sumber, dan tidak boleh ada modul sumber.

##6.2  Modul Standar
Python memiliki library modul standar yang dideskripsikan di dokumen terpisah yaitu Python Library Reference. Beberapa modul sudah dibuat di dalam interpreter; hal ini menyediakan akses ke operasi yang bukan merupakan bagian dari inti language yang bertujuan untuk efisiensi atau untuk menyediakan akses ke primitives sistem operasi. Contohnya, modul `winreg` hanya disediakan di sistem Windows. Ada juga modul yang sudah dibuat di setiap Python interpreter yaitu `sys`. Variabel `sys.ps1 `dan `sys.ps2` mendefinisikan string yang digunakan sebagai prompt primary dan secondary.

##6.3 Fungsi dir()
Fungsi bawaan `dir()` digunakan untuk mencari tahu nama-nama yang ditentukan oleh modul. Dimana fungsi ini mengembalikan `list string `yang diurutkan.

##6.4 Packages
Package adalah sebuah penataan namespace modul Python dengan menggunakan "dotted module names" (nama modul yang diberi tanda titik). Contohnya, modul bernama `A.B` menandai sebuah submodule bernama `B` di dalam package bernama `A`.
ketika kita ingin merancang koleksi modul `(Paket)` untuk penanganan berkas suara dan data suara yang seragam. Ada banyak format berkas suara yang berbeda (biasanya dikenali oleh ekstensi mereka, misalnya `.wav, .aiff, .au)`, jadi kita mungkin perlu membuat dan memelihara koleksi modul yang terus bertambah untuk konversi antara berbagai format file. 

##6.4.1 Mengimpor  Dari Paket
Sekarang apa yang terjadi ketika pengguna menulis from sound.effects import *? Idealnya, orang akan berharap bahwa ini entah bagaimana keluar ke sistem file, menemukan submodul mana yang ada dalam paket, dan mengimpor semuanya. Ini bisa memakan waktu lama dan mengimpor submodul mungkin memiliki efek samping yang tidak diinginkan yang seharusnya hanya terjadi ketika submodul diimport secara eksplisit.

Satu-satunya solusi adalah bagi pembuat paket untuk memberikan indeks paket secara eksplisit. Pernyataan import menggunakan konvensi berikut:

jika suatu paket punya kode `__init __.py` yang mendefinisikan daftar bernama `__all__`, itu diambil sebagai daftar nama modul yang harus diimport ketika `from package import * ditemukan`. Terserah pembuat paket untuk tetap memperbarui daftar ini ketika versi baru dari paket dirilis.
Atau Pembuat paket juga dapat memutuskan untuk tidak mendukungnya, jika mereka tidak melihat penggunaan untuk mengimport * dari paket mereka. Sebagai contoh, berkas `sound/effects/__init__.py `
Jika `__all__ `tidak didefinisikan, pernyataan from sound.effects import * tidak mengimport semua submodul dari paket `sound.effects` ke namespace saat ini; itu hanya memastikan bahwa paket `sound.effects` telah diimport (mungkin menjalankan kode inisialisasi apa pun di` __init__.py`) dan kemudian mengimport nama apa pun yang didefinisikan dalam paket. Ini termasuk semua nama yang didefinisikan (dan submodul yang dimuat secara eksplisit) oleh `__init__.py`. hal itu juga termasuk semua submodul dari paket yang secara eksplisit dimuat oleh sebelumnya pernyataan `import`.

##4.2.2 Referensi Intra-paket
Ketika paket disusun menjadi `subpaket `(seperti pada paket sound pada contoh), Kita dapat menggunakan `import absolut` untuk merujuk pada submodul dari siblings packages. Misalnya, jika modul sound.filters.vocoder perlu menggunakan modul echo dalam  `paket sound.effects`, hal tersebut dapat menggunakan `from sound.effects import echo.`

Kita juga dapat menulis `import relatif`, dengan bentuk` from module import name `pada pernyataan` import`. Import ini menggunakan titik-titik di awalan untuk menunjukkan paket saat ini dan induk yang terlibat dalam `import relatif`.

##6.4.3. Package di dalam Beberapa Direktori
Package mendukung special attribute yaitu `__path__. __path__` diinisialisasi sebagai list berisi nama direktori yang memegang `__init__`.py di sebuah package sebelum kode di file tersebut dieksekusi. Variabel ini bisa dimodifikasi; yang jika dilakukan akan memengaruhi pencarian untuk` modul` dan `subpackage` yang ada di dalam package. Walau fitur `__path__` ini jarang dibutuhkan, tetap saja fitur tersebut dapat diandalkan untuk memperluas kumpulan modul dan `subpackage`.