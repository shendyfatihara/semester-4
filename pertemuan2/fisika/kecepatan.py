class KecepatanRataRata:
    def __init__(self, jarak, waktu):
        self.jarak = jarak
        self.waktu = waktu
    
    def hitung_kecepatan(self):
        return self.jarak / self.waktu

# Contoh penggunaan
kecepatan = KecepatanRataRata(100, 2)
print("Kecepatan Rata-rata:", kecepatan.hitung_kecepatan(), "m/s")
