from barang import Barang

def menu():
    db = Barang(host="localhost", user="root", password="", database="barang")
    
    while True:
        print("\n==== MENU BARANG ====")
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Ubah Barang")
        print("4. Hapus Barang")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            db.connect()
            kode = input("Kode Barang: ")
            nama = input("Nama Barang: ")
            kategori = input("Kategori: ")
            harga = input("Harga: ")
            db.tambah_barang(kode, nama, kategori, harga)
            db.disconnect()

        elif pilihan == '2':
            db.run()

        elif pilihan == '3':
            try:
                db.connect()
                id_barang = int(input("ID Barang yang ingin diubah: "))
                kode = input("Kode Barang Baru: ")
                nama = input("Nama Barang Baru: ")
                kategori = input("Kategori Baru: ")
                harga = input("Harga Baru: ")
                db.ubah_barang(id_barang, kode, nama, kategori, harga)
                db.disconnect()
            except ValueError:
                print("ID harus berupa angka!")

        elif pilihan == '4':
            try:
                db.connect()
                id_barang = int(input("ID Barang yang ingin dihapus: "))
                db.hapus_barang(id_barang)
                db.disconnect()
            except ValueError:
                print("ID harus berupa angka!")

        elif pilihan == '5':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    menu()
