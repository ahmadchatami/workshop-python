**Bab 5**
**Data Struktur**
pada bab ini menjelaskan beberapa hal yang telah Anda pelajari pada bab-bab yang kemaren secara lebih rinci, dan menambahkan beberapa hal baru juga.

5.1. More on Lists
 Berikut adalah semua metode objek daftar:
 - list.append(x)
 	Tambahkan item ke akhir daftar. Setara dengan a[len(a):] = [x]  

- list.extend(iterable)
	Perluas daftar dengan menambahkan semua item dari iterable. Setara dengan a[len(a):] = dapat diubah.

- list.insert(i, x)
	Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen yang akan disisipkan sebelumnya, jadi a.insert(0, x) disisipkan di depan daftar, dan a.insert(len(a), x) setara dengan a.append( x).
	
- list.remove(x)
	Hapus item pertama dari daftar yang nilainya sama dengan x. Ini menimbulkan ValueError jika tidak ada item seperti itu.
	
- list.pop([i])
	Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop() menghapus dan mengembalikan item terakhir dalam daftar. (Kurung siku di sekitar i dalam tanda tangan metode menunjukkan bahwa parameternya opsional, bukan berarti Anda harus mengetikkan tanda kurung siku pada posisi itu. Anda akan sering melihat notasi ini di Referensi Pustaka Python.)
	
- list.clear()
	Hapus semua item dari daftar. Setara dengan del a[:].
	
- list.index(x[, start[, end]])
	Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x. Menaikkan ValueError jika tidak ada item seperti itu.

	Argumen opsional mulai dan akhir ditafsirkan seperti dalam notasi irisan dan digunakan untuk membatasi pencarian ke urutan daftar tertentu. Indeks yang dikembalikan dihitung relatif terhadap awal urutan penuh daripada argumen awal.
	
- list.count(x)
Kembalikan berapa kali x muncul dalam daftar.

- list.sort(*, key=None,reverse=False)
Urutkan item dari daftar di tempat (argumen dapat digunakan untuk penyesuaian pengurutan, lihat diurutkan() untuk penjelasannya).

- list.reverse()
Balikkan elemen daftar di tempatnya.

- list.copy()
Kembalikan salinan daftar yang dangkal. Setara dengan [:].
     Tambahkan item ke akhir daftar. Setara dengan a[len(a):] = [x]  

- list.extend(iterable)
	
    Perluas daftar dengan menambahkan semua item dari iterable. Setara dengan a[len(a):] = dapat diubah.

- list.insert(i, x)
	
    Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen yang akan disisipkan sebelumnya, jadi a.insert(0, x) disisipkan di depan daftar, dan a.insert(len(a), x) setara dengan a.append( x).
	
- list.remove(x)
	
    Hapus item pertama dari daftar yang nilainya sama dengan x. Ini menimbulkan ValueError jika tidak ada item seperti itu.
	
- list.pop([i])
	
    Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop() menghapus dan mengembalikan item terakhir dalam daftar. (Kurung siku di sekitar i dalam tanda tangan metode menunjukkan bahwa parameternya opsional, bukan berarti Anda harus mengetikkan tanda kurung siku pada posisi itu. Anda akan sering melihat notasi ini di Referensi Pustaka Python.)
	
- list.clear()
	
    Hapus semua item dari daftar. Setara dengan del a[:].
	
- list.index(x[, start[, end]])
	
    Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x. Menaikkan ValueError jika tidak ada item seperti itu.

	Argumen opsional mulai dan akhir ditafsirkan seperti dalam notasi irisan dan digunakan untuk membatasi pencarian ke urutan daftar tertentu. Indeks yang dikembalikan dihitung relatif terhadap awal urutan penuh daripada argumen awal.
	
- list.count(x)

    Kembalikan berapa kali x muncul dalam daftar.

- list.sort(*, key=None,reverse=False)

    Urutkan item dari daftar di tempat (argumen dapat digunakan untuk penyesuaian pengurutan, lihat diurutkan() untuk penjelasannya).

- list.reverse()

    Balikkan elemen daftar di tempatnya.

- list.copy()

    Kembalikan salinan daftar yang dangkal. Setara dengan [:].
    
 ppend(). Untuk mengambil item dari atas tumpukan, gunakan pop() tanpa indeks eksplisit.

5.1.3 daftar list comprehensions Pemahaman daftar list comprehensions menyediakan cara singkat untuk membuat daftar. Pemahaman daftar list comprehension terdiri dari tanda kurung yang berisi ekspresi diikuti oleh klausa for, lalu nol atau lebih klausa for atau if. Hasilnya akan menjadi daftar baru yang dihasilkan dari mengevaluasi ekspresi dalam konteks dari klausa for dan if yang mengikutinya.

5.2 pernyataan del Peryataan ‘def’ adalah kata kunci yang digunakan untuk mendefinisikan sebuah fungsi. Fungsi sendiri adalah kelompok kode yang dapat digunakan kembali di bagian program yang lain. Sebab Python adalah bahasa pemrograman multi-paradigma, dalam paradigma OOP (pemrograman berorientasi objek), kata kunci ‘def’ digunakan juga untuk mendefinisikan ‘method’ alias fungsi dalam sebuah ‘class’.

5.3 tuples and urutan sequences Operasi indexing and slicing operations adalah dua contoh tipe data sequence (lihat Sequence Types --- list, tuple, range). Karena python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lain: tuple. tuple sering digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda. Tuples adalah immutable, dan biasanya berisi urutan elemen yang heterogen yang diakses melalui unpacking (lihat nanti di bagian ini) atau pengindeksan (atau bahkan berdasarkan atribut dalam kasus namedtuples <collections.namedtuple> ). Daftar adalah :term:mutable(), dan elemen-elemennya biasanya homogen dan diakses dengan menyusuri iterating daftar list.

5.4 himpunan set Himpunan atau Set adalah koleksi yang tidak terurut tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Kurung kurawal atau fungsi set() dapat digunakan untuk membuat himpunan.

5.5 dictionaries Operasi utama pada dictionary adalah menyimpan nilai dengan beberapa kunci key dan mengekstraksi nilai yang diberikan kunci key. Dimungkinkan juga untuk menghapus pasangan kunci:nilai dengan del. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci itu dilupakan.

5.6 looping techniques • Fungsi items() digunakan untuk mengakses pasangan dari setiap elemen dan nilai-nya yang terdapat di dalam dicionary. • Fungsi enumerate() mengembalikan nilai berupa objek enumerate. Objek enumerate sendiri merupakan objek iterable yang tiap itemnya berpasangan dengan indeks atau angka yang mewakilinya. Dengan kata lain fungsi ini akan menambahkan penghitung (indeks) ke objek iterable dan mengembalikannya. • Math merupakan nodul bawaan dari python untuk memperluas daftar fungsi matematika. Setelah mengimpor math modul, anda dapat mulai menggunakan metode dan konstanta.
    