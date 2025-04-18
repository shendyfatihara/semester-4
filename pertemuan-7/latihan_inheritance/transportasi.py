class AlatTransportasi:
    def bergerak(self):
        print("Alat transportasi sedang bergerak...")

class Pesawat(AlatTransportasi):
    def bergerak(self):
        print("Pesawat terbang di angkasa!")

class Kapal(AlatTransportasi):
    def bergerak(self):
        print("Kapal berlayar di lautan!")

# Contoh penggunaan
pesawat = Pesawat()
kapal = Kapal()

pesawat.bergerak()  # Output: Pesawat terbang di angkasa!
kapal.bergerak()    # Output: Kapal berlayar di lautan!