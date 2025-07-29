
---

# 🏥 Aplikasi Streamlit: Cek Data Rumah Sakit Indonesia

Aplikasi berbasis **Streamlit** ini memungkinkan pengguna untuk mengecek dan menampilkan data rumah sakit di seluruh provinsi di Indonesia secara interaktif.

---

## 🎯 Fitur Aplikasi

### 🏠 1. **General (Halaman Utama)**

Fitur-fitur:

* ✅ Menampilkan **seluruh data rumah sakit** dalam bentuk tabel (`st.dataframe`).
* ✅ Menampilkan **deskripsi statistik** dari dataset (`data.describe()`).
* ✅ Menampilkan **informasi struktur data** (seperti tipe data dan non-null values) menggunakan `data.info()` (perlu dicatat bahwa `data.info()` tidak langsung bisa ditampilkan di Streamlit, perlu dialihkan ke `st.text` atau `io.StringIO`).
* ✅ Menampilkan **grafik batang (bar chart)** sebaran jumlah rumah sakit per provinsi.
* ✅ Menampilkan **tabel peringkat provinsi berdasarkan jumlah rumah sakit**.
* ✅ Menampilkan **distribusi kepemilikan rumah sakit** dalam bentuk tabel (jenis kepemilikan vs jumlah).

---

### 🗺️ 2. **Cek Data Provinsi**

Fitur-fitur:

* ✅ Pilihan **provinsi** melalui `selectbox`.
* ✅ Menampilkan **jumlah rumah sakit** di provinsi terpilih.
* ✅ Menampilkan **data rumah sakit spesifik provinsi** dalam bentuk tabel.
* ✅ Menampilkan **pie chart distribusi kelas rumah sakit** (misalnya kelas A, B, C) di provinsi yang dipilih.
* ✅ Tabel distribusi kelas rumah sakit.

---

### 🏙️ 3. **Cek Data Kabupaten**

Fitur-fitur:

* ✅ Pilihan **kabupaten/kota** melalui `selectbox`.
* ✅ Menampilkan **jumlah rumah sakit** di kabupaten terpilih.
* ✅ Menampilkan **data rumah sakit** di kabupaten terpilih.

---


## 🧰 Teknologi yang Digunakan

| Library   | Versi  |
| --------- | ------ |
| Streamlit | 1.45.0 |
| Pandas    | 2.2.3  |
| NumPy     | 1.24.3 |

---

## 📁 Struktur Proyek

```
cek-rs-indonesia/
├── apps.py                 # File utama aplikasi Streamlit
├── Hospital_Indonesia_datasets.csv    # Dataset rumah sakit Indonesia
├── requirements.txt       # Daftar library yang digunakan
└── README.md              # Dokumentasi proyek
```

---

## 🚀 Cara Menjalankan Aplikasi

### 1. **Persiapan Virtual Environment (opsional tapi disarankan)**

```bash
python3 -m venv env
source env/bin/activate      # macOS/Linux
env\Scripts\activate         # Windows
```

### 2. **Instalasi Library yang Dibutuhkan**

Pastikan Anda berada di folder proyek.

```bash
pip install -r requirements.txt
```

**Jika belum memiliki file `requirements.txt`, buat dengan isi:**

```txt
streamlit==1.45.0
pandas==2.2.3
numpy==1.24.3
```

Lalu install:

```bash
pip install -r requirements.txt
```

### 3. **Jalankan Aplikasi Streamlit**

```bash
streamlit run apps.py
```

Tunggu beberapa detik, browser akan terbuka otomatis menampilkan aplikasi.

---

