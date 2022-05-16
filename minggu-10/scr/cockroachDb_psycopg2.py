#Menggunakan Cockroach Tanpa server(beta)

# Kloning repo GitHub kode sampel:

'''
git clone https://github.com/cockroachlabs/hello-world-python-psycopg2
'''

# Instal driver psycopg2

'''
pip install psycopg2-binary
'''

# Jalankan kode

#setel DATABASE_URLvariabel lingkungan ke string koneksi ke cluster CockroachDB Cloud:
'''
export DATABASE_URL="{connection-string}"
'''

#menjalankan kode
'''
cd hello-world-python-psycopg2
'''

'''
python example.py
'''

#output:
"""
Balances at Fri Oct 30 18:27:00 2020:
(1, 1000)
(2, 250)
Balances at Fri Oct 30 18:27:00 2020:
(1, 900)
(2, 350)
"""