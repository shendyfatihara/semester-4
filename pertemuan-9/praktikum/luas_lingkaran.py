import math

class Lingkaran:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def luas(self):
        return math.pi * (self.__radius ** 2)

lingkaran = Lingkaran(5)
print(lingkaran.luas)  # Output: 78.53981633974483