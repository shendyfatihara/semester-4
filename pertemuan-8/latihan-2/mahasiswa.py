class Mahasiswa:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create(self, nim, nama, jk, prodi):
        cursor = self.db_connection.connection.cursor()
        try:
            sql = "INSERT INTO mahasiswa (nim, nama, jk, prodi) VALUES (%s, %s, %s, %s)"
            values = (nim, nama, jk, prodi)
            cursor.execute(sql, values)
            self.db_connection.connection.commit()
            print("Data mahasiswa berhasil ditambahkan.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def read_all(self):
        cursor = self.db_connection.connection.cursor()
        try:
            cursor.execute("SELECT id, nim, nama, jk, prodi FROM mahasiswa")
            results = cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()

    def update(self, id, nim, nama, jk, prodi):
        cursor = self.db_connection.connection.cursor()
        try:
            sql = "UPDATE mahasiswa SET nim=%s, nama=%s, jk=%s, prodi=%s WHERE id=%s"
            values = (nim, nama, jk, prodi, id)
            cursor.execute(sql, values)
            self.db_connection.connection.commit()
            print("Data mahasiswa berhasil diupdate.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def delete(self, id):
        cursor = self.db_connection.connection.cursor()
        try:
            sql = "DELETE FROM mahasiswa WHERE id=%s"
            cursor.execute(sql, (id,))
            self.db_connection.connection.commit()
            print("Data mahasiswa berhasil dihapus.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
