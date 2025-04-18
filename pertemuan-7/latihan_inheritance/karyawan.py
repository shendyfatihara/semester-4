class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def info(self):
        print(f"Nama: {self.nama}, Gaji: {self.gaji}")

class Manager(Karyawan):
    def __init__(self, nama, gaji, departemen):
        super().__init__(nama, gaji)
        self.departemen = departemen

    def info(self):
        super().info()
        print(f"Departemen: {self.departemen}")

class Programmer(Karyawan):
    def __init__(self, nama, gaji, bahasa):
        super().__init__(nama, gaji)
        self.bahasa = bahasa

    def info(self):
        super().info()
        print(f"Bahasa Pemrograman: {self.bahasa}")

# Contoh penggunaan
manager = Manager("Budi", 15000000, "IT")
programmer = Programmer("Andi", 12000000, "Python")

manager.info()
programmer.info()
