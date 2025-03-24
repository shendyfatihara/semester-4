class Tekanan:
    def __init__(self, gaya, luas):
        self.gaya = gaya
        self.luas = luas
    
    def hitung_tekanan(self):
        return self.gaya / self.luas

# Contoh penggunaan
tekanan = Tekanan(100, 2)
print("Tekanan:", tekanan.hitung_tekanan(), "Pascal")
