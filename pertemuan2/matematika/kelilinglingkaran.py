import math

class Lingkaran:
    def __init__(self, radius):
        self.radius = radius
    
    def hitung_keliling(self):
        return 2 * math.pi * self.radius

# Contoh penggunaan
lingkaran = Lingkaran(7)
print("Keliling Lingkaran:", lingkaran.hitung_keliling())
