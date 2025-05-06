class Panjang:
    def __init__(self, meter):
        self.__meter = meter

    @property
    def kilometer(self):
        return self.__meter / 1000

    @kilometer.setter
    def kilometer(self, kilometer):
        self.__meter = kilometer * 1000

panjang = Panjang(5000)
print(panjang.kilometer)  # Output: 5.0
panjang.kilometer = 3
print(panjang.kilometer)  # Output: 3.0