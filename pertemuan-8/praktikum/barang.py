from connection import DatabaseConnection
import mysql.connector

class Barang(DatabaseConnection):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def tambah_barang(self, kodebrg, namabrg, kategori, harga):
        try:
            if self.connection:
                cursor = self.connection.cursor()
                query = "INSERT INTO barang (kodebrg, namabrg, kategori, harga) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (kodebrg, namabrg, kategori, harga))
                self.connection.commit()
                cursor.close()
                print("Barang berhasil ditambahkan.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def tampilkan_semua(self):
        try:
            if self.connection:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM barang")
                hasil = cursor.fetchall()
                cursor.close()
                return hasil
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def ubah_barang(self, id, kodebrg, namabrg, kategori, harga):
        try:
            if self.connection:
                cursor = self.connection.cursor()
                query = "UPDATE barang SET kodebrg=%s, namabrg=%s, kategori=%s, harga=%s WHERE id=%s"
                cursor.execute(query, (kodebrg, namabrg, kategori, harga, id))
                self.connection.commit()
                cursor.close()
                print("Barang berhasil diubah.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def hapus_barang(self, id):
        try:
            if self.connection:
                cursor = self.connection.cursor()
                query = "DELETE FROM barang WHERE id=%s"
                cursor.execute(query, (id,))
                self.connection.commit()
                cursor.close()
                print("Barang berhasil dihapus.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def run(self):
        self.connect()
        data = self.tampilkan_semua()

        print("\nData Barang:")
        print("-" * 75)
        print(f"{'ID':<5} {'Kode':<10} {'Nama':<25} {'Kategori':<15} {'Harga':<10}")
        print("-" * 75)

        for row in data:
            id, kode, nama, kategori, harga = row
            print(f"{id:<5} {kode:<10} {nama:<25} {kategori:<15} {harga:<10}")

        print("-" * 75)
        self.disconnect()