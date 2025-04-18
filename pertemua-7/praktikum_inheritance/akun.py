class Akun:
    def __init__(self, username):
        self.username = username

    def info(self):
        print(f"Username: {self.username}")

class AkunBisnis(Akun):
    def __init__(self, username, nama_bisnis):
        super().__init__(username)
        self.nama_bisnis = nama_bisnis

    def info(self):
        super().info()
        print(f"Nama Bisnis: {self.nama_bisnis}")

# Contoh penggunaan
akun = AkunBisnis("johndoe", "Kopi Kenangan")
akun.info()
