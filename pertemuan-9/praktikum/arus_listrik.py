class KecepatanListrik:
    def __init__(self, tegangan, hambatan):
        self.__tegangan = tegangan
        self.__hambatan = hambatan

    @property
    def arus(self):
        return self.__tegangan / self.__hambatan

listrik = KecepatanListrik(120, 24)
print(listrik.arus)  # Output: 5.0
