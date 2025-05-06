class Sensor:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):  # Hanya getter (read-only)
        return self.__data

sensor = Sensor(42)
print(sensor.data)        # Output: 42
# sensor.data = 100       # Error! Tidak punya setter