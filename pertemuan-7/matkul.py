class MataKuliah:
    def __init__(self, nama):
        self.nama = nama

    def info(self):
        print(f"Nama Mata Kuliah: {self.nama}")

class KuliahOnline(MataKuliah):
    def __init__(self, nama, platform):
        super().__init__(nama)
        self.platform = platform

    def info(self):
        super().info()
        print(f"Platform: {self.platform}")

# Contoh penggunaan
matkul = KuliahOnline("Pemrograman Python", "Zoom")
matkul.info()
