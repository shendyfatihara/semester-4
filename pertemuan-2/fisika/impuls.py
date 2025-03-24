class Impuls:
    def __init__(self, gaya, waktu):
        self.gaya = gaya
        self.waktu = waktu
    
    def hitung_impuls(self):
        return self.gaya * self.waktu

# Contoh penggunaan
impuls = Impuls(20, 5)
print("Impuls:", impuls.hitung_impuls(), "N.s")
