class Kecepatan:
    def __init__(self, jarak, waktu):
        self.__jarak = jarak
        self.__waktu = waktu

    @property
    def kecepatan(self):
        return self.__jarak / self.__waktu

kecepatan = Kecepatan(100, 2)
print(kecepatan.kecepatan)  # Output: 50.0