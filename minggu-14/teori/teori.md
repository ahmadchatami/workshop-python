## An introduction to machine learning with scikit-learn
#### Machine learning setting masalah
masalah pembelajaran mempertimbangkan satu set n sampel data dan kemudian mencoba memprediksi sifat data yang tidak diketahui. Jika setiap sampel lebih dari satu angka dan, misalnya, entri multidimensi (alias data multivariat), dikatakan memiliki beberapa atribut atau fitur.
##### Masalah belajar terbagi dalam beberapa kategori:
- `supervised learning`, di mana data dilengkapi dengan atribut tambahan yang ingin kami prediksi (Klik di sini untuk membuka halaman pembelajaran terawasi scikit-belajar). Masalah ini dapat berupa:
klasifikasi:
    -  sampel milik dua atau lebih kelas dan kami ingin belajar dari data yang sudah berlabel bagaimana memprediksi kelas data yang tidak berlabel. Contoh masalah klasifikasi adalah pengenalan digit tulisan tangan, di mana tujuannya adalah untuk menetapkan setiap vektor input ke salah satu dari sejumlah kategori diskrit yang terbatas
regresi:
    -  jika output yang diinginkan terdiri dari satu atau lebih variabel kontinu, maka tugas tersebut disebut regresi. Contoh masalah regresi adalah prediksi panjang ikan salmon sebagai fungsi dari umur dan beratnya.

- `unsupervised learning`, di mana data pelatihan terdiri dari satu set vektor input x tanpa nilai target yang sesuai. Tujuan dalam masalah tersebut mungkin untuk menemukan kelompok contoh serupa dalam data, yang disebut pengelompokan, atau untuk menentukan distribusi data dalam ruang input, yang dikenal sebagai estimasi kepadatan, atau untuk memproyeksikan data dari dimensi tinggi. ruang hingga dua atau tiga dimensi untuk tujuan visualisasi

####  Loading an example dataset
`scikit-learn` hadir dengan beberapa kumpulan data standar, misalnya kumpulan data `iris` dan `angka` untuk klasifikasi dan kumpulan `diabetes dataset` untuk regresi.Konvensi notasi kami adalah bahwa `$` menunjukkan prompt shell sementara `>>>`

```
$ python
>>> from sklearn import datasets
>>> iris = datasets.load_iris()
>>> digits = datasets.load_digits()
````

Dataset adalah objek seperti kamus yang menyimpan semua data dan beberapa metadata tentang data tersebut. Data ini disimpan dalam anggota `.data`, yang merupakan array `n_samples`,` n_features`. Dalam kasus masalah yang diawasi, satu atau lebih variabel respons disimpan di anggota `.target`. Rincian lebih lanjut tentang kumpulan data yang berbeda dapat ditemukan di `edicated section`.
````
>>> print(digits.data)
[[ 0.   0.   5. ...   0.   0.   0.]
 [ 0.   0.   0. ...  10.   0.   0.]
 [ 0.   0.   0. ...  16.   9.   0.]
 ...
 [ 0.   0.   1. ...   6.   0.   0.]
 [ 0.   0.   2. ...  12.   0.   0.]
 [ 0.   0.  10. ...  12.   1.   0.]]
 ````
 ````
 >>> digits.target
array([0, 1, 2, ..., 8, 9, 8])
````

#### Learning and predicting
Dalam `scikit-learn`, estimator untuk klasifikasi adalah objek Python yang mengimplementasikan metode `fit(X, y)` dan `predict(T)`. Contoh estimator adalah kelas `sklearn.svm.SVC`, yang mengimplementasikan `support vector classification`. Konstruktor estimator mengambil parameter model sebagai argumen.
kami akan mempertimbangkan estimator sebagai kotak hitam:
````
>>> from sklearn import svm
>>> clf = svm.SVC(gamma=0.001, C=100.)
````
Contoh estimator `clf` (untuk pengklasifikasi) pertama-tama dipasang ke model; yaitu, ia harus belajar dari model. Ini dilakukan dengan meneruskan set pelatihan kami ke metode `fit`. Untuk set pelatihan, kami akan menggunakan semua gambar dari dataset kami, kecuali untuk gambar terakhir, yang akan kami simpan untuk prediksi kami. Kami memilih set pelatihan dengan sintaks `[:-1]` Python, yang menghasilkan array baru yang berisi semua kecuali item terakhir dari `digits.data:`
````
>>> clf.fit(digits.data[:-1], digits.target[:-1])
SVC(C=100.0, gamma=0.001)

>>> clf.predict(digits.data[-1:])
array([8])
````
##### Conventions
`scikit-learn estimator` mengikuti aturan tertentu untuk membuat perilaku mereka lebih prediktif. Ini dijelaskan secara lebih rinci dalam Daftar Istilah Umum dan `Elemen API`
    - Type casting.

    
    >>> import numpy as np
    >>> from sklearn import kernel_approximation
    >>> rng = np.random.RandomState(0)
    >>> X = rng.rand(10, 2000)
    >>> X = np.array(X, dtype='float32')
    >>> X.dtype
    dtype('float32')

    >>> transformer = kernel_approximation.RBFSampler()
    >>> X_new = transformer.fit_transform(X)
    >>> X_new.dtype
    dtype('float64')
Dalam contoh ini, X adalah float32, yang dilemparkan ke float64 oleh fit_transform(X).
Target regresi dilemparkan ke float64 dan target klasifikasi dipertahankan:
````
>>> from sklearn import datasets
>>> from sklearn.svm import SVC
>>> iris = datasets.load_iris()
>>> clf = SVC()
>>> clf.fit(iris.data, iris.target)
SVC()

>>> list(clf.predict(iris.data[:3]))
[0, 0, 0]

>>> clf.fit(iris.data, iris.target_names[iris.target])
SVC()

>>> list(clf.predict(iris.data[:3]))
['setosa', 'setosa', 'setosa']
````
yang pertama `predict(`) mengembalikan array integer, karena `iris .target` (array integer) digunakan `fit`. `Predict(`) kedua mengembalikan array string, karena `iris.target_names` adalah untuk pemasangan.

##### Refitting and updating parameters
`Hyper-parameter` dari estimator dapat diperbarui setelah dibuat melalui metode `set_params()`. Memanggil `fit()` lebih dari sekali akan menimpa apa yang dipelajari oleh `fit()` sebelumnya:
````
>>> import numpy as np
>>> from sklearn.datasets import load_iris
>>> from sklearn.svm import SVC
>>> X, y = load_iris(return_X_y=True)

>>> clf = SVC()
>>> clf.set_params(kernel='linear').fit(X, y)
SVC(kernel='linear')
>>> clf.predict(X[:5])
array([0, 0, 0, 0, 0])

>>> clf.set_params(kernel='rbf').fit(X, y)
SVC()
>>> clf.predict(X[:5])
array([0, 0, 0, 0, 0])
````
#### Multiclass vs. multilabel fitting
Saat menggunakan pengklasifikasi multikelas, tugas pembelajaran dan prediksi yang dilakukan bergantung pada format data target yang sesuai dengan:
````
>>> from sklearn.svm import SVC
>>> from sklearn.multiclass import OneVsRestClassifier
>>> from sklearn.preprocessing import LabelBinarizer

>>> X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
>>> y = [0, 0, 1, 1, 2]

>>> classif = OneVsRestClassifier(estimator=SVC(random_state=0))
>>> classif.fit(X, y).predict(X)
array([0, 0, 1, 1, 2])
````
Perhatikan bahwa contoh keempat dan kelima mengembalikan semua nol, menunjukkan bahwa mereka tidak cocok dengan tiga label yang cocok. Dengan keluaran multilabel, sebuah instance juga dapat diberi beberapa label:
````
>>> from sklearn.preprocessing import MultiLabelBinarizer
>>> y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
>>> y = MultiLabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
array([[1, 1, 0, 0, 0],
       [1, 0, 1, 0, 0],
       [0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0],
       [1, 0, 1, 0, 0]])
````
Dalam hal ini, pengklasifikasi cocok pada instance yang masing-masing diberi beberapa label.   `MultiLabelBinarizer` digunakan untuk menggabungkan `array 2d` dari multilabel agar sesuai. Akibatnya, `predict()` mengembalikan larik 2d dengan beberapa label prediksi untuk setiap instance.    