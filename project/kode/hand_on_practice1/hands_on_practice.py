"""
Data Engineering - Pengenalan Library Utama
Contoh penggunaan library dasar untuk data engineering
"""

# 1. Python Standard Library
import os
import json
import csv
import datetime
import logging

# 2. Pandas dan Numpy
import pandas as pd
import numpy as np

# 3. Requests dan BeautifulSoup
import requests
from bs4 import BeautifulSoup

# 4. Database
import sqlite3
from sqlalchemy import create_engine

# 5. Luigi untuk workflow
import luigi

# ========== 1. PYTHON STANDARD LIBRARY ==========
def demo_standard_library():
    print("\n=== Demo Python Standard Library ===")
    
    # File handling
    with open('sample.txt', 'w') as f:
        f.write("Hello Data Engineering!")
    
    # JSON handling
    data = {
        'nama': 'John Doe',
        'usia': 25,
        'kota': 'Jakarta'
    }
    
    # Menulis JSON
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    # Membaca JSON
    with open('data.json', 'r') as f:
        loaded_data = json.load(f)
    print("Data JSON:", loaded_data)
    
    # Datetime
    sekarang = datetime.datetime.now()
    print("Waktu sekarang:", sekarang.strftime("%Y-%m-%d %H:%M:%S"))

# ========== 2. PANDAS & NUMPY ==========
def demo_pandas_numpy():
    print("\n=== Demo Pandas & Numpy ===")
    
    # Membuat DataFrame
    df = pd.DataFrame({
        'nama': ['John', 'Jane', 'Bob'],
        'usia': [25, 30, 35],
        'kota': ['Jakarta', 'Surabaya', 'Bandung']
    })
    print("\nDataFrame Dasar:")
    print(df)
    
    # Operasi dasar Pandas
    print("\nInfo DataFrame:")
    print(df.info())
    
    print("\nStatistik Deskriptif:")
    print(df.describe())
    
    # Numpy array
    arr = np.array([1, 2, 3, 4, 5])
    print("\nNumpy Array:", arr)
    print("Mean:", np.mean(arr))
    print("Std Dev:", np.std(arr))

# ========== 3. WEB SCRAPING ==========
def demo_web_scraping():
    print("\n=== Demo Web Scraping ===")
    
    # Contoh scraping sederhana
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Mendapatkan judul buku pertama
        books = soup.find_all('h3')
        print("\nContoh judul buku:")
        for book in books[:3]:
            print(book.text.strip())
    else:
        print("Gagal mengakses website")

# ========== 4. DATABASE ==========
def demo_database():
    print("\n=== Demo Database ===")
    
    # SQLite
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    
    # Membuat tabel
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mahasiswa
    (id INTEGER PRIMARY KEY,
     nama TEXT,
     usia INTEGER,
     kota TEXT)
    ''')
    
    # Insert data
    cursor.execute('''
    INSERT INTO mahasiswa (nama, usia, kota)
    VALUES (?, ?, ?)
    ''', ('John Doe', 25, 'Jakarta'))
    
    conn.commit()
    
    # Query data
    cursor.execute('SELECT * FROM mahasiswa')
    print("\nData dari SQLite:")
    for row in cursor.fetchall():
        print(row)
    
    conn.close()
    
    # SQLAlchemy
    engine = create_engine('sqlite:///sample.db')
    df = pd.read_sql_query('SELECT * FROM mahasiswa', engine)
    print("\nData menggunakan SQLAlchemy:")
    print(df)

# ========== 5. LUIGI WORKFLOW ==========
class GenerateData(luigi.Task):
    date = luigi.DateParameter(default=datetime.date.today())
    
    def output(self):
        return luigi.LocalTarget(f'data_{self.date}.txt')
    
    def run(self):
        with self.output().open('w') as f:
            f.write(f"Data generated on {self.date}")

class ProcessData(luigi.Task):
    date = luigi.DateParameter(default=datetime.date.today())
    
    def requires(self):
        return GenerateData(self.date)
    
    def output(self):
        return luigi.LocalTarget(f'processed_{self.date}.txt')
    
    def run(self):
        with self.input().open('r') as fin, self.output().open('w') as fout:
            data = fin.read()
            fout.write(f"Processed: {data}")

def demo_luigi():
    print("\n=== Demo Luigi Workflow ===")
    print("Luigi workflow siap dijalankan dengan:")
    print("luigi.build([ProcessData()])")

# ========== MAIN PROGRAM ==========
if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    try:
        # Menjalankan demo
        demo_standard_library()
        demo_pandas_numpy()
        demo_web_scraping()
        demo_database()
        demo_luigi()
        
        logging.info("Semua demo berhasil dijalankan!")
        
    except Exception as e:
        logging.error(f"Terjadi error: {str(e)}")
