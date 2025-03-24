class EnergiKinetik:
    def __init__(self, massa, kecepatan):
        self.massa = massa
        self.kecepatan = kecepatan
    
    def hitung_energi_kinetik(self):
        return 0.5 * self.massa * (self.kecepatan ** 2)

# Contoh penggunaan
kinetik = EnergiKinetik(10, 20)
print("Energi Kinetik:", kinetik.hitung_energi_kinetik(), "Joule")
