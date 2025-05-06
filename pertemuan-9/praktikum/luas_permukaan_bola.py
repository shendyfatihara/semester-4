import math

class Bola:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def luas_permukaan(self):
        return 4 * math.pi * (self.__radius ** 2)

bola = Bola(3)
print(bola.luas_permukaan)  # Output: 113.097335