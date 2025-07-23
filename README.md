# 🏁 Tugas Akhir (TA) - Final Project

**Nama Mahasiswa**: Aida Fitrania Prabasati  
**NRP**: 5025211033  
**Judul TA**: Fine-Tuning Model Transformer untuk Pengenalan Emosi pada Lirik Lagu Berbahasa Indonesia Berdasarkan Model Emosi Russell  
**Dosen Pembimbing**: Ratih Nur Esti Anggraini, S.Kom., M.Sc., Ph.D.  
**Dosen Ko-pembimbing**: Ir. Adhatus Solichah Ahmadiyah, S.Kom., M.Sc.

---

## 📺 Demo Aplikasi  

[![Demo Aplikasi](https://github.com/Informatics-ITS/ta-aidafitraniaa/blob/main/Overview.png)](https://www.youtube.com/watch?v=seicLEdF4MU)  
*Klik gambar di atas untuk menonton demo*

---

## Tentang Tugas Akhir

Tugas Akhir ini bertujuan untuk mengeksplorasi dan membandingkan performa tiga model transformer yaitu IndoBERT, RoBERTa, dan DistilBERT dalam tugas klasifikasi emosi pada lirik lagu berbahasa Indonesia. Emosi dikategorikan berdasarkan Model Emosi Russell ke dalam empat kelas: senang, sedih, tenang, dan marah.  

Untuk mengetahui pengaruh preprocessing dan penyeimbangan data, dilakukan fine-tuning ketiga model menggunakan empat skenario berbeda, yaitu:  
1. Tanpa Oversampling & Full Preprocessing  
2. Tanpa Oversampling & Tanpa Full Preprocessing ( Tanpa Stopword Removal & Stemming )
3. Oversampling & Full Preprocessing
4. Oversampling & Tanpa Full Preprocessing ( Tanpa Stopword Removal & Stemming )

Proses penelitian ini mencakup beberapa tahap utama:  
[![Demo Aplikasi](https://github.com/Informatics-ITS/ta-aidafitraniaa/blob/main/diagram alir.png)]


## 🛠 Panduan Instalasi & Menjalankan Software  

### Prasyarat  
- Daftar dependensi (contoh):
  - Python 3.10+
  - Node.js v18+
  - MySQL 8.0
  - [Lainnya...]

### Langkah-langkah  
1. **Clone Repository**  
   ```bash
   git clone https://github.com/Informatics-ITS/TA.git
   ```
2. **Instalasi Dependensi**
   ```bash
   cd [folder-proyek]
   pip install -r requirements.txt  # Contoh untuk Python
   npm install  # Contoh untuk Node.js
   ```
3. **Konfigurasi**
- Salin/rename file .env.example menjadi .env
- Isi variabel lingkungan sesuai kebutuhan (database, API key, dll.)
4. **Jalankan Aplikasi**
   ```bash
   python main.py  # Contoh untuk Python
   npm start      # Contoh untuk Node.js
   ```
5. Buka browser dan kunjungi: `http://localhost:3000` (sesuaikan dengan port proyek Anda)

---

## 📚 Dokumentasi Tambahan

- [![Dokumentasi API]](docs/api.md)
- [![Diagram Arsitektur]](docs/architecture.png)
- [![Struktur Basis Data]](docs/database_schema.sql)

---

## ✅ Validasi


---

## ⁉️ Pertanyaan?

Hubungi:
- Penulis: [fitraniap78@gmail.com]
- Pembimbing Utama: [ratih@its.ac.id]
