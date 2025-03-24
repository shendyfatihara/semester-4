import math

class Kubus:
    def __init__(self, sisi):
        if sisi <= 0:
            raise ValueError("Sisi kubus harus lebih besar dari 0.")
        self.sisi = sisi

    def volume(self):
        return self.sisi ** 3

    def luas_permukaan(self):
        return 6 * (self.sisi ** 2)

try:
    sisi = float(input("Masukkan panjang sisi kubus: "))
    kubus = Kubus(sisi)

    print(f"Volume kubus: {kubus.volume()}")
    print(f"Luas permukaan kubus: {kubus.luas_permukaan()}")

except ValueError as ve:
    print(f"Kesalahan Input: {ve}")

except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")

finally:
    print("Terima kasih telah menggunakan Kalkulator Kubus.")