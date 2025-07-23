# 🏁 Tugas Akhir (TA) - Final Project

**Nama Mahasiswa**: Aida Fitrania Prabasati  
**NRP**: 5025211033  
**Judul TA**: Fine-Tuning Model Transformer untuk Pengenalan Emosi pada Lirik Lagu Berbahasa Indonesia Berdasarkan Model Emosi Russell  
**Dosen Pembimbing**: Ratih Nur Esti Anggraini, S.Kom., M.Sc., Ph.D.  
**Dosen Ko-pembimbing**: Ir. Adhatus Solichah Ahmadiyah, S.Kom., M.Sc.

---

## 📺 Demo Aplikasi  

[![Demo Aplikasi](./Overview.png)](https://www.youtube.com/watch?v=seicLEdF4MU)  
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

![Demo Aplikasi](./diagram%20alir.png)

1. Pengumpulan dan anotasi dataset sebanyak 1.500 lirik lagu pop Indonesia (tahun 2000–2025)
  
  |              Judul Lagu                 | Penyanyi      | Genre     |           Lirik Lagu ( Penggalang Lirik )                          | Tahun Rilis | Label Emosi |
  |-----------------------------------------|---------------|-----------|--------------------------------------------------------------------|-------------|-------------|
  |Bagaimana Kalau Aku Tidak Baik Baik Saja | Judika        | Pop       | “Andai aku bisa memutar waktu<br>Aku tak ingin mengenalmu....”     |     2021    |    Sedih    |
  |Tak Ada Ujungnya                         | Rony Parulian | Pop       | “Ku temukan satu sisi dalam diri<br>Warna warni penuhi jiwaku....” |     2024    |   Senang    |
  |Semua Aku Dirayakan                      | Nadin Amizah  | Pop, Folk | “Terima kasih, katanya<br>Semua aku dirayakan...."                 |     2023    |   Tenang    |
  |Penipu Hati                              | Tata Janeeta  | Pop       | "Kau katakan kau tak ingin<br>Membagi hatimu....."                 |     2014    |    Marah    |
  |               ...                       |    ...        |   ...     |                         ...                                        |    ...      |    ...      |                                                          
                                                                  
  
3. Preprocessing, termasuk pembersihan, normalisasi, stopword removal, dan stemming
4. Balancing data menggunakan metode oversampling ( Random Over Sampling )
5. Fine-tuning model transformer
6. Evaluasi performa model menggunakan 5-Fold Cross Validation dan metrik accuracy, precision, recall, dan F1-score


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
