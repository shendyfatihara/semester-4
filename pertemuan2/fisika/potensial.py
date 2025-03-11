class EnergiPotensial:
    def __init__(self, massa, tinggi, gravitasi=9.8):
        self.massa = massa
        self.tinggi = tinggi
        self.gravitasi = gravitasi
    
    def hitung_energi_potensial(self):
        return self.massa * self.gravitasi * self.tinggi

# Contoh penggunaan
potensial = EnergiPotensial(10, 5)
print("Energi Potensial:", potensial.hitung_energi_potensial(), "Joule")
