import math

class Lingkaran:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius harus lebih besar dari 0.")
        self.radius = radius

    def luas(self):
        return math.pi * (self.radius ** 2)

    def keliling(self):
        return 2 * math.pi * self.radius

try:
    radius = float(input("Masukkan radius lingkaran: "))
    lingkaran = Lingkaran(radius)
    print(f"Luas lingkaran: {lingkaran.luas():.2f}")
    print(f"Keliling lingkaran: {lingkaran.keliling():.2f}")
except ValueError as ve:
    print(f"Kesalahan Input: {ve}")
except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")
finally:
    print("Terima kasih telah menggunakan Kalkulator Lingkaran.")
