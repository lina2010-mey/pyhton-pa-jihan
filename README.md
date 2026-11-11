# Python untuk Pemula

## Deskripsi
Proyek ini berisi latihan dasar pemrograman Python untuk pemula. Materi disusun mulai dari pengenalan Python hingga penggunaan virtual environment dan konfigurasi IDE.

## Tujuan Pembelajaran
Setelah menyelesaikan materi ini, diharapkan dapat memahami dasar-dasar pemrograman Python dan mampu membuat serta menjalankan program sederhana.

## Daftar Materi

1. Pengenalan dan Instalasi Python
2. Variabel dan Tipe Data
3. Operator pada Python
4. Kondisi If Else
5. Perulangan
6. Lists dan Dictionaries
7. Function
8. Class dan Object
9. PIP dan Virtual Environments
10. Konfigurasi Environment dan IDE
11. README.md dan Requirements.txt

## Contoh Program

Contoh penggunaan kondisi:

```python
nilai = 80

if nilai >= 90:
    print("A")
elif nilai >= 70:
    print("B")
else:
    print("C")
```

Hasil:
```text
B
```

## Cara Menjalankan Program

1. Buka terminal Arch Linux.
2. Masuk ke folder proyek.
3. Aktifkan virtual environment:

```bash
source venv/bin/activate
```

4. Jalankan salah satu file Python, contohnya:

```bash
python hello.py
```

5. Untuk keluar dari virtual environment:

```bash
deactivate
```

## Struktur Folder

- `screenshots/` — Dokumentasi hasil pengerjaan.
- `venv/` — Virtual environment Python.
- `hello.py` dan file `.py` lainnya — Contoh latihan Python.
- `requirements.txt` — Daftar dependensi proyek.
- `.gitignore` — Daftar file dan folder yang tidak dilacak Git.

## Perintah Terminal Penting

| Perintah | Fungsi |
|---|---|
| `pwd` | Melihat lokasi folder saat ini |
| `ls` | Melihat daftar file |
| `cd nama_folder` | Masuk ke folder |
| `cd ..` | Kembali ke folder sebelumnya |
| `python nama.py` | Menjalankan program Python |
| `clear` | Membersihkan tampilan terminal |
| `exit` | Keluar dari terminal |

## Penutup

Proyek ini dibuat sebagai latihan untuk memahami dasar-dasar pemrograman Python menggunakan Arch Linux dan Visual Studio Code.