### Responsi
1.  Membaca file csv langsung dengan cara menggunakan link
````
import pandas as pd

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv"
df = pd.read_csv(url)
````
2. menampilkan data dari file csv
````
df.head()
````
3. untuk mengecek index data csv
````
df.index
````
4. untuk index transposing data
````
df.T
````