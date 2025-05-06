class Suhu:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def kelvin(self):
        return self.__celsius + 273.15

    @kelvin.setter
    def kelvin(self, nilai):
        self.__celsius = nilai - 273.15

suhu = Suhu(0)
print(suhu.kelvin)  # Output: 273.15