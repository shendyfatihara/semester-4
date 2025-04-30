import mysql.connector

class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Database connected successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def disconnect(self):
        if self.connection:
            self.connection.close()

class Mahasiswa:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def fetch_all(self):
        cursor = self.db_connection.connection.cursor()
        try:
            cursor.execute("SELECT id, nim, nama, jk, prodi FROM mahasiswa")
            results = cursor.fetchall()
            return results
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            cursor.close()

class App:
    def __init__(self):
        self.db = DatabaseConnection(
            host="localhost",
            user="root",
            password="",
            database="mahasiswa"
        )
        self.mahasiswa = None

    def run(self):
        self.db.connect()
        self.mahasiswa = Mahasiswa(self.db)
        data = self.mahasiswa.fetch_all()

        print("\nData Mahasiswa:")
        print("-" * 68)
        print(f"{'ID':<5} {'NIM':<15} {'Nama':<20} {'JK':<5} {'Prodi':<10}")
        print("-" * 68)

        for row in data:
            id, nim, nama, jk, prodi = row
            print(f"{id:<5} {nim:<15} {nama:<20} {jk:<5} {prodi:<10}")

        print("-" * 68)
        self.db.disconnect()

if __name__ == "__main__":
    app = App()
    app.run()
