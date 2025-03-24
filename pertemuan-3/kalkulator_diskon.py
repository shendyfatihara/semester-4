class Diskon:
    def __init__(self, harga_awal, diskon_persen):
        if harga_awal <= 0 or diskon_persen < 0:
            raise ValueError("Harga awal harus lebih besar dari 0 dan diskon tidak boleh negatif.")
        self.harga_awal = harga_awal
        self.diskon_persen = diskon_persen

    def hitung_diskon(self):
        return self.harga_awal * (self.diskon_persen / 100)

    def harga_setelah_diskon(self):
        return self.harga_awal - self.hitung_diskon()

try:
    harga_awal = float(input("Masukkan harga awal: "))
    diskon_persen = float(input("Masukkan persentase diskon: "))
    diskon = Diskon(harga_awal, diskon_persen)
    print(f"Jumlah diskon: {diskon.hitung_diskon()}")
    print(f"Harga setelah diskon: {diskon.harga_setelah_diskon()}")
except ValueError as ve:
    print(f"Kesalahan Input: {ve}")
except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")
finally:
    print("Terima kasih telah menggunakan Kalkulator Diskon.")
