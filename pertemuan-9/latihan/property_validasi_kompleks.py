class Suhu:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, nilai):
        if nilai >= -459.67:  # Absolute zero Fahrenheit
            self.__celsius = (nilai - 32) * 5/9
        else:
            print("Suhu tidak valid!")

suhu = Suhu(0)
print(suhu.fahrenheit)  # Output: 32.0
suhu.fahrenheit = 212
print(suhu.fahrenheit)  # Output: 212.0