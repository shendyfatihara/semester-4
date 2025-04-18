class Bentuk:
    def hitung_keliling(self):
        pass

class Segitiga(Bentuk):
    def __init__(self, sisi1, sisi2, sisi3):
        self.sisi1 = sisi1
        self.sisi2 = sisi2
        self.sisi3 = sisi3

    def hitung_keliling(self):
        return self.sisi1 + self.sisi2 + self.sisi3

class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

# Contoh penggunaan
segitiga = Segitiga(3, 4, 5)
persegi_panjang = PersegiPanjang(6, 4)

print(f"Keliling Segitiga: {segitiga.hitung_keliling()}")
print(f"Keliling Persegi Panjang: {persegi_panjang.hitung_keliling()}")
