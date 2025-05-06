class Mobil:
    def __init__(self, merek):
        self.__merek = merek  # Akan diubah menjadi _Mobil__merek

mobil = Mobil("Honda")
# print(mobil.__merek)  # Error!
print(mobil._Mobil__merek)  # Output: Honda (name mangling)
