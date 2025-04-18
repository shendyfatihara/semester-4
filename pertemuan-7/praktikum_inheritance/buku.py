class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def info(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")

class Novel(Buku):
    def __init__(self, judul, penulis, genre):
        super().__init__(judul, penulis)
        self.genre = genre

    def info(self):
        super().info()
        print(f"Genre: {self.genre}")

# Contoh penggunaan
novel = Novel("Laskar Pelangi", "Andrea Hirata", "Drama")
novel.info()

