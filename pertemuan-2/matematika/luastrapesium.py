class Trapesium:
    def __init__(self, sisi_atas, sisi_bawah, tinggi):
        self.sisi_atas = sisi_atas
        self.sisi_bawah = sisi_bawah
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return 0.5 * (self.sisi_atas + self.sisi_bawah) * self.tinggi

# Contoh penggunaan
trapesium = Trapesium(6, 8, 4)
print("Luas Trapesium:", trapesium.hitung_luas())