class HukumOhm:
    def __init__(self, arus, hambatan):
        self.__arus = arus
        self.__hambatan = hambatan

    @property
    def tegangan(self):
        return self.__arus * self.__hambatan

    @tegangan.setter
    def tegangan(self, tegangan_baru):
        self.__arus = tegangan_baru / self.__hambatan

ohm = HukumOhm(2, 10)
print(ohm.tegangan)  # Output: 20
ohm.tegangan = 40
print(ohm.tegangan)  # Output: 40