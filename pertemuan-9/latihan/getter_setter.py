class Produk:
    def __init__(self, nama, harga):
        self.__nama = nama
        self.__harga = harga

    def get_harga(self):  # Getter
        return self.__harga

    def set_harga(self, harga_baru):  # Setter
        if harga_baru > 0:
            self.__harga = harga_baru
        else:
            print("Harga tidak valid!")

produk = Produk("Laptop", 10000000)
print(produk.get_harga())       # Output: 10000000
produk.set_harga(12000000)
print(produk.get_harga())       # Output: 12000000