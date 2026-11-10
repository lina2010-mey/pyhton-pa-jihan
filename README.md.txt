Materi	Penjelasan Singkat	Contoh
Variabel	Tempat menyimpan data.	nama = "Aris"
Tipe Data	Jenis data dalam Python.	int, str, float, bool
Output	Menampilkan informasi.	print("Halo")
Input	Memasukkan data dari pengguna.	input("Nama: ")
Operator	Melakukan operasi matematika atau perbandingan.	+, -, *, /
Kondisional	Menentukan keputusan berdasarkan kondisi.	if, elif, else
Perulangan	Mengulang perintah.	for, while
Fungsi	Mengelompokkan kode agar bisa digunakan kembali.	def halo():


Contoh Kondisional
nilai = 80if nilai >= 90:    print("A")elif nilai >= 70:    print("B")else:    print("C")


Hasil: B
Contoh Perulangan
for i in range(5):    print(i)


Hasil:
0
1
2
3
4

2. Petunjuk Menjalankan Program di Arch Linux
Ikuti langkah berikut secara berurutan.

Langkah 1 – Masuk ke folder Python
cd ~/python-untuk-pemula

Langkah 2 – Aktifkan virtual environment
source venv/bin/activate

Langkah 3 – Buat file Python

Contoh:
nano latihan.py

Langkah 4 – Masukkan kode program
print("Halo, saya sedang belajar Python!")


Langkah 5 – Simpan file

Tekan:
- CTRL + O
- Enter
- CTRL + X
Langkah 6 – Jalankan program
python latihan.py

Hasilnya:
Halo, saya sedang belajar Python!

3. Perintah Penting di Terminal Arch Linux
Perintah	Fungsi
pwd	Melihat lokasi folder saat ini.
ls	Melihat daftar file.
cd nama_folder	Masuk ke folder.
cd ..	Kembali ke folder sebelumnya.
nano nama.py	Membuat atau mengedit file Python.
python nama.py	Menjalankan program Python.
clear	Membersihkan tampilan terminal.
exit	Keluar dari terminal.