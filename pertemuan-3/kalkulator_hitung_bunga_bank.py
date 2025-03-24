class BungaBank:
    def __init__(self, pokok, bunga, tahun):
        if pokok <= 0 or bunga <= 0 or tahun <= 0:
            raise ValueError("Pokok, bunga, dan tahun harus lebih besar dari 0.")
        self.pokok = pokok
        self.bunga = bunga
        self.tahun = tahun

    def hitung_bunga(self):
        return self.pokok * (self.bunga / 100) * self.tahun

    def total_bayar(self):
        return self.pokok + self.hitung_bunga()

try:
    pokok = float(input("Masukkan jumlah pokok (uang yang disimpan): "))
    bunga = float(input("Masukkan suku bunga per tahun (dalam %): "))
    tahun = int(input("Masukkan jangka waktu (dalam tahun): "))
    bunga_bank = BungaBank(pokok, bunga, tahun)
    print(f"Bunga yang diterima: {bunga_bank.hitung_bunga()}")
    print(f"Total yang harus dibayar setelah {tahun} tahun: {bunga_bank.total_bayar()}")
except ValueError as ve:
    print(f"Kesalahan Input: {ve}")
except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")
finally:
    print("Terima kasih telah menggunakan Kalkulator Bunga Bank.")
