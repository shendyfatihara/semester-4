class Musik:
    def __init__(self, judul):
        self.judul = judul

    def info(self):
        print(f"Judul Lagu: {self.judul}")

class LaguJazz(Musik):
    def __init__(self, judul, instrumen):
        super().__init__(judul)
        self.instrumen = instrumen

    def info(self):
        super().info()
        print(f"Instrumen Utama: {self.instrumen}")

# Contoh penggunaan
lagu = LaguJazz("Autumn Leaves", "Saxophone")
lagu.info()

