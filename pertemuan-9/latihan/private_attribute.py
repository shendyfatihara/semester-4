class Karyawan:
    def __init__(self, nama, gaji):
        self._nama = nama  # Protected (bisa diakses, tapi sebaiknya tidak langsung)
        self.__gaji = gaji  # Private (tidak bisa diakses langsung)

karyawan = Karyawan("Budi", 5000000)
print(karyawan._nama)  # Output: Budi (bisa diakses, tapi tidak disarankan)
# print(karyawan.__gaji)  # Error! AttributeError