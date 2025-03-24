class Daya:
    def __init__(self, usaha, waktu):
        self.usaha = usaha
        self.waktu = waktu
    
    def hitung_daya(self):
        return self.usaha / self.waktu

# Contoh penggunaan
daya = Daya(200, 10)
print("Daya:", daya.hitung_daya(), "Watt")
