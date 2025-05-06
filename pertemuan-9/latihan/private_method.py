class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __kali(self):  # Private method
        return self.a * self.b

    def hasil_kali(self):  # Public method untuk mengakses __kali
        return self.__kali()

kalk = Kalkulator(4, 5)
# print(kalk.__kali())  # Error!
print(kalk.hasil_kali())  # Output: 20