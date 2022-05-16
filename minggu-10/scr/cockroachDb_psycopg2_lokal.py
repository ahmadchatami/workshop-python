#menggunakan cluster lokal

#menjalankan perintah
'''
cockroach start-single-node --advertise-addr 'localhost' --insecure
'''

#perhatikan informasi koneksi pada shell SQL:
'''
CockroachDB node starting at 2021-08-30 17:25:30.06524 +0000 UTC (took 4.3s)
build:               CCL v21.1.6 @ 2021/07/20 15:33:43 (go1.15.11)
webui:               http://localhost:8080
sql:                 postgresql://root@localhost:26257?sslmode=disable
'''

#kemudian dilanjutkan dengan mendapatkan kode sampel pada kloning repo Github
#pada cockroachDb_psycopg2.py