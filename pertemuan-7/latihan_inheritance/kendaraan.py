class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

    def info(self):
        print(f"Merk: {self.merk}")

class Mobil(Kendaraan):
    def __init__(self, merk, jumlah_pintu):
        super().__init__(merk)
        self.jumlah_pintu = jumlah_pintu

    def info(self):
        super().info()
        print(f"Jumlah Pintu: {self.jumlah_pintu}")

class Motor(Kendaraan):
    def __init__(self, merk, jenis):
        super().__init__(merk)
        self.jenis = jenis

    def info(self):
        super().info()
        print(f"Jenis: {self.jenis}")

# Contoh penggunaan
mobil = Mobil("Toyota", 4)
motor = Motor("Honda", "Sport")

mobil.info()
motor.info()
