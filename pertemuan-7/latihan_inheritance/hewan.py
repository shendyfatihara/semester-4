class Hewan:
    def __init__(self, nama):
        self.nama = nama
    def bersuara(self):
        print(f"{self.nama} bersuara.")
class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.nama} mengeong: Meow!")
class Anjing(Hewan):
    def bersuara(self):
        print(f"{self.nama} menggonggong: Woof!")
# Contoh penggunaan
kucing = Kucing("Kitty")
anjing = Anjing("Doggy")
kucing.bersuara()
anjing.bersuara()
