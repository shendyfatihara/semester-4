class BangunDatar:
    def luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 3.14 * (self.jari_jari ** 2)

# Contoh penggunaan
persegi = Persegi(5)
lingkaran = Lingkaran(7)

print(f"Luas Persegi: {persegi.luas()}")
print(f"Luas Lingkaran: {lingkaran.luas()}")
