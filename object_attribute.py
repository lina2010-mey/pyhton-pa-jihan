class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna


mobil1 = Mobil("Toyota", "Hitam")

print("Merek mobil:", mobil1.merek)
print("Warna mobil:", mobil1.warna)
