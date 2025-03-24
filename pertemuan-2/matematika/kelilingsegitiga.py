class Segitiga:
    def __init__(self, sisi_a, sisi_b, sisi_c):
        self.sisi_a = sisi_a
        self.sisi_b = sisi_b
        self.sisi_c = sisi_c
    
    def hitung_keliling(self):
        return self.sisi_a + self.sisi_b + self.sisi_c

# Contoh penggunaan
segitiga = Segitiga(3, 4, 5)
print("Keliling Segitiga:", segitiga.hitung_keliling())
