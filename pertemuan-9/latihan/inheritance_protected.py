class Kendaraan:
    def __init__(self, roda):
        self._roda = roda  # Protected (bisa diakses subclass)

class Motor(Kendaraan):
    def info_roda(self):
        return f"Motor punya {self._roda} roda."

motor = Motor(2)
print(motor.info_roda())  # Output: Motor punya 2 roda.