class MassaJenis:
    def __init__(self, massa, volume):
        self.__massa = massa
        self.__volume = volume

    @property
    def massa_jenis(self):
        return self.__massa / self.__volume

massa_jenis = MassaJenis(100, 5)
print(massa_jenis.massa_jenis)  # Output: 20.0