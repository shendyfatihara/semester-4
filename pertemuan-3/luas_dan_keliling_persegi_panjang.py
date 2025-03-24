class PersegiPanjang:
    def __init__(self, panjang, lebar):
        if panjang <= 0 or lebar <= 0:
            raise ValueError("Panjang dan lebar harus lebih besar dari 0.")
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

try:
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    persegi_panjang = PersegiPanjang(panjang, lebar)
    print(f"Luas persegi panjang: {persegi_panjang.luas()}")
    print(f"Keliling persegi panjang: {persegi_panjang.keliling()}")
except ValueError as ve:
    print(f"Kesalahan Input: {ve}")
except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")
finally:
    print("Terima kasih telah menggunakan Kalkulator Persegi Panjang.")