class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    
    def hitung_keliling(self):
        return 4 * self.sisi

# Contoh penggunaan
persegi = Persegi(5)
print("Keliling Persegi:", persegi.hitung_keliling())
