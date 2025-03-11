class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

# Contoh penggunaan
segitiga = Segitiga(6, 8)
print("Luas Segitiga:", segitiga.hitung_luas())
