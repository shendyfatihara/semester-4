class Minuman:
    def __init__(self, nama):
        self.nama = nama

    def sajikan(self):
        print(f"Minuman {self.nama} siap disajikan!")

class Kopi(Minuman):
    def sajikan(self):
        print(f"Kopi {self.nama} disajikan panas dengan aroma wangi!")

class Jus(Minuman):
    def sajikan(self):
        print(f"Jus {self.nama} disajikan dingin dengan es batu!")

# Contoh penggunaan
kopi = Kopi("Arabika")
jus = Jus("Jeruk")

kopi.sajikan()  # Output: Kopi Arabika disajikan panas dengan aroma wangi!
jus.sajikan()   # Output: Jus Jeruk disajikan dingin dengan es batu!
