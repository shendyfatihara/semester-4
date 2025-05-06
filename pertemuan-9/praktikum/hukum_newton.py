class HukumNewton:
    def __init__(self, massa, percepatan):
        self.__massa = massa
        self.__percepatan = percepatan

    @property
    def gaya(self):
        return self.__massa * self.__percepatan

    @gaya.setter
    def gaya(self, gaya_baru):
        self.__percepatan = gaya_baru / self.__massa

newton = HukumNewton(10, 5)
print(newton.gaya)  # Output: 50
newton.gaya = 100
print(newton.gaya)  # Output: 100