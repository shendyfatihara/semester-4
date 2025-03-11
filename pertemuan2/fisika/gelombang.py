class KecepatanGelombang:
    def __init__(self, panjang_gelombang, frekuensi):
        self.panjang_gelombang = panjang_gelombang
        self.frekuensi = frekuensi
    
    def hitung_kecepatan(self):
        return self.panjang_gelombang * self.frekuensi

# Contoh penggunaan
gelombang = KecepatanGelombang(2, 50)
print("Kecepatan Gelombang:", gelombang.hitung_kecepatan(), "m/s")
