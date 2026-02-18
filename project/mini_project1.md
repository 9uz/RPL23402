# Mini Project: Data Source Analysis

## Project Overview

**Tujuan**: Menganalisis tiga jenis sumber data berbeda untuk memahami karakteristik dan potensi penggunaannya dalam konteks bisnis.
**Mini Project**: Data Source Analysis

- Menganalisis 3 sumber data berbeda (structured, semi-structured, unstructured)
- Membuat dokumentasi karakteristik masing-masing dan peloajari dokumen
- Mengidentifikasi potensi use cases
- tambahkan kode pembacaan data dan gambar tiap data
- kumpulokan dalam bentuk pdf

**Durasi**: 2-3 jam

# 1. Analisis Data Terstruktur (Structured Data)

### 1.1 Deskripsi Sumber Data

- Nama Database/Dataset:
- Format:
- Ukuran Data:
- Sumber:

### 1.2 Karakteristik

- Schema/Struktur:
- Tipe Data:
- Relasi antar Data:
- Kualitas Data:
- Frekuensi Update:

### 1.3 Potensi Use Cases

- Use Case 1:

  - Deskripsi:
  - Manfaat Bisnis:
  - Technical Requirements:
- Use Case 2:

  - Deskripsi:
  - Manfaat Bisnis:
  - Technical Requirements:

## 2. Analisis Data Semi-Terstruktur (Semi-structured Data)

### 2.1 Deskripsi Sumber Data

- Nama Dataset/File:
- Format:
- Ukuran Data:
- Sumber:

### 2.2 Karakteristik

- Format Spesifik:
- Struktur Data:
- Flexibilitas:
- Challenges:
- Aksesibilitas:

### 2.3 Potensi Use Cases

- Use Case 1:

  - Deskripsi:
  - Manfaat Bisnis:
  - Technical Requirements:
- Use Case 2:

  - Deskripsi:
  - Manfaat Bisnis:
  - Technical Requirements:

## 3. Analisis Data Tidak Terstruktur (Unstructured Data)

### 3.1 Deskripsi Sumber Data

- Tipe Data:
- Format:
- Ukuran Data:
- Sumber:

### 3.2 Karakteristik

- Kompleksitas:
- Storage Requirements:
- Processing Challenges:
- Data Quality Issues:
- Accessibility:

### 3.3 Potensi Use Cases

- Use Case 1:

  - Deskripsi:
  - Manfaat Bisnis:
  - Technical Requirements:
- Use Case 2:

  - Deskripsi:
  - Manfaat Bisnis:
  - Technical Requirements:

## 4. Kesimpulan dan Rekomendasi

### 4.1 Ringkasan Temuan

- Structured Data:
- Semi-structured Data:
- Unstructured Data:

### 4.2 Rekomendasi

- Technical Recommendations:
- Business Recommendations:
- Implementation Priorities:

### 4.3 Next Steps

- Short-term Actions:
- Long-term Planning:
- Resource Requirements:

## 5. Lampiran

- Data Samples
- Technical Documentation
- Reference Materials

---

---

Berikut contoh pengisian untuk analisis data terstruktur, semi-terstruktur, dan tidak terstruktur:

**1. Analisis Data Terstruktur (Structured Data)**

**1.1 Deskripsi Sumber Data**

* Nama Database/Dataset: **Pasien Rumah Sakit Umum**
* Format: **CSV**
* Ukuran Data: **100 MB**
* Sumber: **Rumah Sakit Umum Daerah** (URL)

**1.2 Karakteristik**

* Schema/Struktur:
  * ID_Pasien (Integer, Primary Key)
  * Nama (Text)
  * Usia (Integer)
  * Jenis Kelamin (Text)
  * Alamat (Text)
  * Diagnosis (Text)
  * Tanggal Periksa (Date)
* Tipe Data: Integer, Text, Date
* Relasi antar Data: Tidak ada relasi antar tabel dalam dataset ini.
* Kualitas Data: Tinggi, data telah diverifikasi dan dibersihkan.
* Frekuensi Update: Bulanan

**1.3 Potensi Use Cases**

* **Use Case 1:**

  * Deskripsi: Analisis tren penyakit berdasarkan usia dan jenis kelamin.
  * Manfaat Bisnis: Membantu rumah sakit dalam mengalokasikan sumber daya dan merencanakan strategi pencegahan penyakit.
  * Technical Requirements: Software analisis data, pengetahuan SQL.
* **Use Case 2:**

  * Deskripsi: Identifikasi pasien dengan diagnosis yang sama untuk penelitian klinis.
  * Manfaat Bisnis: Membantu peneliti dalam menemukan pola dan mengembangkan pengobatan baru.
  * Technical Requirements: Software analisis data, pengetahuan statistik.

**2. Analisis Data Semi-Terstruktur (Semi-structured Data)**

**2.1 Deskripsi Sumber Data**

* Nama Dataset/File: **Log Aktivitas Pengguna Aplikasi Kesehatan**
* Format: **JSON**
* Ukuran Data: **5 GB**
* Sumber: **Aplikasi Kesehatan Mobile** (URL)

**2.2 Karakteristik**

* Format Spesifik: JSON
* Struktur Data: Kumpulan objek dengan key-value pairs, beberapa objek bersarang.
* Flexibilitas: Dapat menampung berbagai jenis data, termasuk teks, angka, tanggal, dan array.
* Challenges: Membutuhkan parsing JSON untuk mengekstrak data yang relevan.
* Aksesibilitas: Dapat diakses melalui API aplikasi kesehatan.

**2.3 Potensi Use Cases**

* **Use Case 1:**

  * Deskripsi: Analisis pola penggunaan aplikasi berdasarkan waktu dan fitur yang digunakan.
  * Manfaat Bisnis: Meningkatkan desain dan fungsionalitas aplikasi.
  * Technical Requirements: Software analisis data, pengetahuan JSON parsing.
* **Use Case 2:**

  * Deskripsi: Identifikasi pengguna yang aktif dan potensial untuk program promosi.
  * Manfaat Bisnis: Meningkatkan engagement pengguna dan penjualan.
  * Technical Requirements: Software analisis data, pengetahuan segmentasi data.

**3. Analisis Data Tidak Terstruktur (Unstructured Data)**

**3.1 Deskripsi Sumber Data**

* Tipe Data: **Teks**
* Format: **Dokumen PDF**
* Ukuran Data: **10 GB**
* Sumber: **Laporan Penelitian Medis** (URL)

**3.2 Karakteristik**

* Kompleksitas: Teks dalam bahasa alami, mengandung informasi medis yang kompleks.
* Storage Requirements: Membutuhkan penyimpanan yang besar.
* Processing Challenges: Membutuhkan teknik Natural Language Processing (NLP) untuk mengekstrak informasi yang relevan.
* Data Quality Issues: Dapat mengandung kesalahan tata bahasa, singkatan, dan istilah medis yang ambigu.
* Accessibility: Dapat diakses melalui software pembaca PDF dan API NLP.

**3.3 Potensi Use Cases**

* **Use Case 1:**

  * Deskripsi: Ekstraksi informasi tentang efek samping obat dari laporan penelitian.
  * Manfaat Bisnis: Membantu peneliti dalam memahami profil keamanan obat.
  * Technical Requirements: Software NLP, pengetahuan domain medis.
* **Use Case 2:**

  * Deskripsi: Identifikasi tren dalam penelitian medis berdasarkan topik dan metodologi.
  * Manfaat Bisnis: Membantu peneliti dalam menemukan peluang penelitian baru.
  * Technical Requirements: Software NLP, pengetahuan visualisasi data.
