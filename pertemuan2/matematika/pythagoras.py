import math

class Pythagoras:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def hitung_hypotenusa(self):
        return math.sqrt(self.a ** 2 + self.b ** 2)

# Contoh penggunaan
pythagoras = Pythagoras(3, 4)
print("Panjang Hipotenusa:", pythagoras.hitung_hypotenusa())
