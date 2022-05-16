#Menggunakan Cockroach Tanpa server(beta)

# Kloning repo GitHub kode sampel:

'''
git clone https://github.com/cockroachlabs/example-app-python-sqlalchemy/
'''

#menggunakan File dbinit.sqlmenginisialisasi skema database yang digunakan aplikasi:
'''
CREATE TABLE accounts (
    id UUID PRIMARY KEY,
    balance INT8
);
'''

#Menggunakan SQLAlchemy models.pyuntuk memetakan Accountstabel ke objek Python:
'''
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
Base = declarative_base()
class Account(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'accounts'
    id = Column(UUID(as_uuid=True), primary_key=True)
    balance = Column(Integer)
'''

#Menggunakan SQLAlchemy main.pyuntuk memetakan metode Python ke operasi SQL:
'''
"""This simple CRUD application performs the following operations sequentially:
    1. Creates 100 new accounts with randomly generated IDs and randomly-computed balance amounts.
    2. Chooses two accounts at random and takes half of the money from the first and deposits it
     into the second.
    3. Chooses five accounts at random and deletes them.
"""
from math import floor
import os
import random
import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from models import Account
# The code below inserts new accounts.
def create_accounts(session, num):
    """Create N new accounts with random account IDs and account balances.
    """
    print("Creating new accounts...")
    new_accounts = []
    while num > 0:
        account_id = uuid.uuid4()
        account_balance = floor(random.random()*1_000_000)
        new_accounts.append(Account(id=account_id, balance=account_balance))
        seen_account_ids.append(account_id)
        print(f"Created new account with id {account_id} and balance {account_balance}.")
        num = num - 1
    session.add_all(new_accounts)
def transfer_funds_randomly(session, one, two):
    """Transfer money between two accounts.
    """
    try:
        source = session.query(Account).filter(Account.id == one).one()
    except NoResultFound:
        print("No result was found")
    except MultipleResultsFound:
        print("Multiple results were found")
    dest = session.query(Account).filter(Account.id == two).first()
    print(f"Random account balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")
    amount = floor(source.balance/2)
    print(f"Transferring {amount} from account {one} to account {two}...")
    # Check balance of the first account.
    if source.balance < amount:
        raise ValueError(f"Insufficient funds in account {one}")
    source.balance -= amount
    dest.balance += amount
    print(f"Transfer complete.\nNew balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")
def delete_accounts(session, num):
    """Delete N existing accounts, at random.
    """
    print("Deleting existing accounts...")
    delete_ids = []
    while num > 0:
        delete_id = random.choice(seen_account_ids)
        delete_ids.append(delete_id)
        seen_account_ids.remove(delete_id)
        num = num - 1
    accounts = session.query(Account).filter(Account.id.in_(delete_ids)).all()
    for account in accounts:
        print(f"Deleted account {account.id}.")
        session.delete(account)
if __name__ == '__main__':
    # For cockroach demo:
    # DATABASE_URL=postgresql://demo:<demo_password>@127.0.0.1:26257?sslmode=require
    # For CockroachCloud:
    # DATABASE_URL=postgresql://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>
    db_uri = os.environ['DATABASE_URL'].replace("postgresql://", "cockroachdb://")
    try:
        engine = create_engine(db_uri)
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")
    seen_account_ids = []
    run_transaction(sessionmaker(bind=engine),
                    lambda s: create_accounts(s, 100))
    from_id = random.choice(seen_account_ids)
    to_id = random.choice([id for id in seen_account_ids if id != from_id])
    run_transaction(sessionmaker(bind=engine),
                    lambda s: transfer_funds_randomly(s, from_id, to_id))
    run_transaction(sessionmaker(bind=engine), lambda s: delete_accounts(s, 5))
'''

#Instal persyaratan aplikasi

#Instal virtualenv:
'''
pip install virtualenv
'''

#Di tingkat atas direktori proyek aplikasi, buat lalu aktifkan lingkungan virtual:
'''
virtualenv env
'''
'''
source env/bin/activate
'''

#Instal modul yang diperlukan ke lingkungan virtual:
'''
pip install -r requirements.txt
'''

#Inisialisasi database

#Setel DATABASE_URLvariabel lingkungan ke string koneksi untuk cluster:
'''
export DATABASE_URL="{connection-string}"
'''

#perintah untuk mengeksekusi pernyataan SQL dalam dbinit.sqlfile:
'''
cat dbinit.sql | cockroach sql --url $DATABASE_URL
'''

#ouput:
"""
CREATE TABLE
Time: 102ms
"""

#Menjalankan kode

'''
python main.py
'''

#output:
"""
Creating new accounts...
Created new account with id 3a8b74c8-6a05-4247-9c60-24b46e3a88fd and balance 248835.
Created new account with id c3985926-5b77-4c6d-a73d-7c0d4b2a51e7 and balance 781972.
...
Created new account with id 7b41386c-11d3-465e-a2a0-56e0dcd2e7db and balance 984387.
Random account balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 800795
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 149861
Transferring 400397 from account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9 to account 4040aeba-7194-4f29-b8e5-a27ed4c7a297...
Transfer complete.
New balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 400398
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 550258
Deleting existing accounts...
Deleted account 41247e24-6210-4032-b622-c10b3c7222de.
Deleted account 502450e4-6daa-4ced-869c-4dff62dc52de.
Deleted account 6ff06ef0-423a-4b08-8b87-48af2221bc18.
Deleted account a1acb134-950c-4882-9ac7-6d6fbdaaaee1.
Deleted account e4f33c55-7230-4080-b5ac-5dde8a7ae41d.
"""

#dalam shell SQL yang terhubung dapat memverikasi bahwa baris berhasil dimasukkan, diperbarui, dihapus:
'''
> SELECT COUNT(*) FROM accounts;
'''
#output:

"""
count
---------
     95
(1 row)
"""