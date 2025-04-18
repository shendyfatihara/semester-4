class Pekerjaan:
    def bekerja(self):
        print("Melakukan pekerjaan umum...")

class Dokter(Pekerjaan):
    def bekerja(self):
        print("Dokter: Memeriksa pasien dan memberikan resep obat.")

class Guru(Pekerjaan):
    def bekerja(self):
        print("Guru: Mengajar murid di kelas.")

# Contoh penggunaan
dokter = Dokter()
guru = Guru()

dokter.bekerja()  # Output: Dokter: Memeriksa pasien dan memberikan resep obat.
guru.bekerja()    # Output: Guru: Mengajar murid di kelas.
