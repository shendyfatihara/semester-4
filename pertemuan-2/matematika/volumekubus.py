class Kubus:
    def __init__(self, sisi):
        self.sisi = sisi
    
    def hitung_volume(self):
        return self.sisi ** 3

# Contoh penggunaan
kubus = Kubus(4)
print("Volume Kubus:", kubus.hitung_volume())
