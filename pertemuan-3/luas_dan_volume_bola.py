import math

class Bola:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius bola harus lebih besar dari 0.")
        self.radius = radius

    def luas_permukaan(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

try:
    radius = float(input("Masukkan radius bola: "))
    bola = Bola(radius)

    print(f"Luas permukaan bola: {bola.luas_permukaan():.2f}")
    print(f"Volume bola: {bola.volume():.2f}")

except ValueError as ve:
    print(f"Kesalahan Input: {ve}")

except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")

finally:
    print("Terima kasih telah menggunakan Kalkulator Bola.")