class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    
    def hitung_luas(self):
        return self.sisi ** 2

# Contoh penggunaan
persegi = Persegi(4)
print("Luas Persegi:", persegi.hitung_luas())
