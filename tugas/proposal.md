# PROPOSAL PROYEK
## Program Rekap dan Analisis Nilai Matematika Kelas

### 1. Latar Belakang

Guru perlu merekap nilai matematika siswa untuk mengetahui
rata-rata, nilai tertinggi, dan nilai terendah kelas.
Jika dilakukan secara manual, proses tersebut membutuhkan
waktu dan berisiko terjadi kesalahan perhitungan.

Oleh karena itu, dirancang program Python sederhana untuk
membantu proses rekap dan analisis nilai siswa.

### 2. Pengguna dan Tujuan

Pengguna:
Guru matematika.

Tujuan:
1. Mempermudah rekap nilai siswa.
2. Menghitung rata-rata nilai kelas.
3. Menentukan nilai tertinggi dan terendah.
4. Menampilkan hasil rekap secara sederhana.

### 3. Ruang Lingkup

Fitur yang dirancang:
1. Memasukkan nama dan nilai siswa.
2. Memeriksa validitas nilai.
3. Menghitung rata-rata nilai.
4. Menentukan nilai tertinggi dan terendah.
5. Menampilkan hasil rekap.

Batasan:
Nilai siswa berada pada rentang 0 sampai 100.
Program hanya digunakan untuk rekap nilai matematika.

### 4. Kebutuhan Program

Kebutuhan fungsional:
- Program menerima nama dan nilai siswa.
- Program memvalidasi nilai.
- Program menghitung statistik nilai.
- Program menampilkan hasil rekap.

Kebutuhan nonfungsional:
- Program mudah digunakan.
- Program memiliki kode yang terstruktur.
- Program menampilkan pesan jika input tidak valid.

### 5. Input, Proses, dan Output

Input:
Nama siswa dan nilai matematika.

Proses:
Memvalidasi data, menghitung rata-rata,
serta mencari nilai tertinggi dan terendah.

Output:
Daftar nilai siswa, rata-rata kelas,
nilai tertinggi, dan nilai terendah.

### 6. Algoritma

1. Mulai.
2. Masukkan nama dan nilai siswa.
3. Periksa apakah nilai berada pada rentang 0-100.
4. Jika valid, simpan data siswa.
5. Hitung rata-rata nilai.
6. Cari nilai tertinggi dan terendah.
7. Tampilkan hasil rekap.
8. Selesai.

### 7. Rancangan Struktur Program

pertemuan14/
├── latihan/
├── tugas/
├── src/
├── data/
├── tests/
├── docs/
├── README.md
└── .gitignore

### 8. Rancangan Fungsi

- input_data(): menerima data siswa.
- validasi_nilai(): memeriksa rentang nilai.
- hitung_rata_rata(): menghitung rata-rata.
- cari_nilai_tertinggi(): mencari nilai tertinggi.
- cari_nilai_terendah(): mencari nilai terendah.
- tampilkan_hasil(): menampilkan hasil rekap.

### 9. Struktur Data

List digunakan untuk menyimpan kumpulan data siswa.
Dictionary dapat digunakan untuk menyimpan nama dan nilai
setiap siswa.
File teks dapat digunakan untuk menyimpan data nilai.

### 10. Test Case

| No. | Kasus Pengujian | Hasil yang Diharapkan |
|---|---|---|
| 1 | Nilai 80 | Data diterima |
| 2 | Nilai 0 | Data diterima |
| 3 | Nilai 100 | Data diterima |
| 4 | Nilai -5 | Data ditolak |
| 5 | Nilai 110 | Data ditolak |
| 6 | Nilai berupa huruf | Input ditolak |
| 7 | Tidak ada data siswa | Pesan data kosong ditampilkan |

### 11. Pembagian Tugas

Proyek dikerjakan secara individu.

Tanggung jawab:
- Menyusun proposal proyek.
- Merancang algoritma.
- Menentukan struktur program.
- Menyusun test case.
- Membuat dokumentasi.
- Mengelola proyek menggunakan Git dan GitHub.

### 12. Jadwal Pengerjaan

Pertemuan 14:
Menyusun proposal dan rancangan program.

Pertemuan 15:
Mengimplementasikan, menguji, dan memperbaiki program.

Pertemuan 16:
Mempresentasikan hasil proyek.

### 13. Repository GitHub

URL GitHub:
https://github.com/Fanipratiwi/pertemuan-14-perancangan-proyek-2225250175

### 14. Kesimpulan

Program Rekap dan Analisis Nilai Matematika Kelas
dirancang untuk membantu guru mengolah nilai siswa
secara lebih mudah dan terstruktur.