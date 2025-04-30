from connection import DatabaseConnection
from mahasiswa import Mahasiswa

class App:
    def __init__(self):
        self.db = DatabaseConnection(
            host="localhost",
            user="root",
            password="", 
            database="mahasiswa"  
        )
        self.mahasiswa = None

    def menu(self):
        while True:
            print("\n=== Menu Mahasiswa ===")
            print("1. Tampilkan semua mahasiswa")
            print("2. Tambah mahasiswa")
            print("3. Update mahasiswa")
            print("4. Hapus mahasiswa")
            print("5. Keluar")

            choice = input("Pilih menu: ")

            if choice == '1':
                self.show_all()
            elif choice == '2':
                self.add_mahasiswa()
            elif choice == '3':
                self.update_mahasiswa()
            elif choice == '4':
                self.delete_mahasiswa()
            elif choice == '5':
                break
            else:
                print("Pilihan tidak valid!")

    def show_all(self):
        data = self.mahasiswa.read_all()
        print("\nData Mahasiswa:")
        print("-" * 60)
        print(f"{'ID':<5} {'NIM':<15} {'Nama':<20} {'JK':<5} {'Prodi':<10}")
        print("-" * 60)
        for row in data:
            id, nim, nama, jk, prodi = row
            print(f"{id:<5} {nim:<15} {nama:<20} {jk:<5} {prodi:<10}")
        print("-" * 60)

    def add_mahasiswa(self):
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        jk = input("Masukkan Jenis Kelamin (L/P): ")
        prodi = input("Masukkan Prodi: ")
        self.mahasiswa.create(nim, nama, jk, prodi)

    def update_mahasiswa(self):
        id = input("Masukkan ID mahasiswa yang ingin diupdate: ")
        nim = input("Masukkan NIM baru: ")
        nama = input("Masukkan Nama baru: ")
        jk = input("Masukkan Jenis Kelamin baru (L/P): ")
        prodi = input("Masukkan Prodi baru: ")
        self.mahasiswa.update(id, nim, nama, jk, prodi)

    def delete_mahasiswa(self):
        id = input("Masukkan ID mahasiswa yang ingin dihapus: ")
        self.mahasiswa.delete(id)

    def run(self):
        self.db.connect()
        self.mahasiswa = Mahasiswa(self.db)
        self.menu()
        self.db.disconnect()

if __name__ == "__main__":
    app = App()
    app.run()
