class Database:
    def __init__(self, data):
        self.__data = data

    def __enkripsi(self, teks):  # Private method
        return teks.upper()  # Simulasi enkripsi sederhana

    def simpan_data(self):
        data_terenkripsi = self.__enkripsi(self.__data)
        print(f"Data disimpan: {data_terenkripsi}")

db = Database("rahasia")
db.simpan_data()  # Output: Data disimpan: RAHASIA
# db.__enkripsi("test")  # Error!