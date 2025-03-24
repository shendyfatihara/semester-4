class KalkulatorKonversiSuhu:

    @staticmethod
    def celsius_ke_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_ke_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

try:
    suhu_celsius = float(input("Masukkan suhu dalam Celsius: "))
    fahrenheit = KalkulatorKonversiSuhu.celsius_ke_fahrenheit(suhu_celsius)
    print(f"{suhu_celsius} Celsius = {fahrenheit:.2f} Fahrenheit")

    suhu_fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    celsius = KalkulatorKonversiSuhu.fahrenheit_ke_celsius(suhu_fahrenheit)
    print(f"{suhu_fahrenheit} Fahrenheit = {celsius:.2f} Celsius")

except ValueError as ve:
    print(f"Kesalahan Input: {ve}")

except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")

finally:
    print("Terima kasih telah menggunakan Kalkulator Konversi Suhu.")