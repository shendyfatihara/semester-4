class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    
    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

# Contoh penggunaan
balok = Balok(3, 5, 7)
print("Volume Balok:", balok.hitung_volume())
