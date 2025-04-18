class PerangkatElektronik:
    def __init__(self, daya):
        self.daya = daya

    def hidupkan(self):
        print(f"Perangkat menyala dengan daya {self.daya} watt.")

class Televisi(PerangkatElektronik):
    def __init__(self, daya, ukuran):
        super().__init__(daya)
        self.ukuran = ukuran

    def info(self):
        print(f"TV {self.ukuran} inci, Daya: {self.daya} watt")

class Kulkas(PerangkatElektronik):
    def __init__(self, daya, kapasitas):
        super().__init__(daya)
        self.kapasitas = kapasitas

    def info(self):
        print(f"Kulkas {self.kapasitas} liter, Daya: {self.daya} watt")

# Contoh penggunaan
tv = Televisi(100, 32)
kulkas = Kulkas(200, 250)

tv.hidupkan()
kulkas.hidupkan()

tv.info()
kulkas.info()