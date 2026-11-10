class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        print("Nama saya:", self.nama)
        print("Saya kelas:", self.kelas)


siswa1 = Siswa("Aris", "11")
siswa2 = Siswa("Desta", "11")

siswa1.perkenalan()
print()
siswa2.perkenalan()
