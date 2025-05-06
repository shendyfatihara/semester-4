class Kubus:
    def __init__(self, sisi):
        self.__sisi = sisi

    @property
    def volume(self):
        return self.__sisi ** 3

kubus = Kubus(3)
print(kubus.volume)  # Output: 27