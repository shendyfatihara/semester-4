class Usaha:
    def __init__(self, gaya, jarak):
        self.gaya = gaya
        self.jarak = jarak
    
    def hitung_usaha(self):
        return self.gaya * self.jarak

# Contoh penggunaan
usaha = Usaha(15, 10)
print("Usaha:", usaha.hitung_usaha(), "Joule")
