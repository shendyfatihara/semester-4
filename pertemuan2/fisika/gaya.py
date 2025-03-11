class Gaya:
    def __init__(self, massa, percepatan):
        self.massa = massa
        self.percepatan = percepatan
    
    def hitung_gaya(self):
        return self.massa * self.percepatan

# Contoh penggunaan
gaya = Gaya(10, 5)
print("Gaya:", gaya.hitung_gaya(), "N")
