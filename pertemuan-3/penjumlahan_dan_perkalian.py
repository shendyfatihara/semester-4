class Kalkulator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def tambah(self):
        return self.a + self.b

    def kurang(self):
        return self.a - self.b

try:
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    kalkulator = Kalkulator(a, b)

    print(f"Hasil penjumlahan: {kalkulator.tambah()}")
    print(f"Hasil pengurangan: {kalkulator.kurang()}")

except ValueError as ve:
    print(f"Kesalahan Input: {ve}")

except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")

finally:
    print("Terima kasih telah menggunakan Kalkulator.")