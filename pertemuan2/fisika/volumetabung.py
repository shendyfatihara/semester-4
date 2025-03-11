import math

class Tabung:
    def __init__(self, radius, tinggi):
        self.radius = radius
        self.tinggi = tinggi
    
    def hitung_volume(self):
        return math.pi * (self.radius ** 2) * self.tinggi

# Contoh penggunaan
tabung = Tabung(3, 7)
print("Volume Tabung:", tabung.hitung_volume(), "m³")
