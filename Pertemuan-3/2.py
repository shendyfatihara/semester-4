class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def kali(self):
        return self.a * self.b

    def bagi(self):
        if self.b == 0:
            raise ZeroDivisionError("Tidak dapat membagi dengan nol.")
        return self.a / self.b

try:
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    kalkulator = Kalkulator(a, b)
    print(f"Hasil perkalian: {kalkulator.kali()}")
    print(f"Hasil pembagian: {kalkulator.bagi()}")
except ZeroDivisionError as zde:
    print(f"Kesalahan Pembagian: {zde}")
except ValueError as ve:
    print(f"Kesalahan Input: {ve}")
except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")
finally:
    print("Terima kasih telah menggunakan Kalkulator.")
