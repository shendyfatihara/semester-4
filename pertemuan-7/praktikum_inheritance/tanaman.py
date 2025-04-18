class Tanaman:
    def __init__(self, nama):
        self.nama = nama

    def info(self):
        print(f"Nama Tanaman: {self.nama}")

class Pohon(Tanaman):
    def __init__(self, nama, tinggi):
        super().__init__(nama)
        self.tinggi = tinggi

    def info(self):
        super().info()
        print(f"Tinggi: {self.tinggi} meter")

# Contoh penggunaan
pohon = Pohon("Mangga", 5)
pohon.info()
