class AkunBank:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):  # Getter
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai):  # Setter
        if nilai >= 0:
            self.__saldo = nilai
        else:
            print("Saldo tidak boleh negatif!")

akun = AkunBank(500000)
print(akun.saldo)       # Output: 500000 (seolah-olah atribut biasa)
akun.saldo = 750000     # Mengubah nilai via setter
print(akun.saldo)       # Output: 750000