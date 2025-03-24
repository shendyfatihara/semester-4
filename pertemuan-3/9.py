class KonversiSuhu:
    @staticmethod
    def celsius_ke_fahrenheit(celsius):
        return (celsius * 9/5) + 32


    @staticmethod
    def fahrenheit_ke_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

try:
    suhu = float(input("Masukkan suhu dalam Celsius: "))
    fahrenheit = KonversiSuhu.celsius_ke_fahrenheit(suhu)
    print(f"{suhu} Celsius = {fahrenheit:.2f} Fahrenheit")
    
    suhu_fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    celsius = KonversiSuhu.fahrenheit_ke_celsius(suhu_fahrenheit)
    print(f"{suhu_fahrenheit} Fahrenheit = {celsius:.2f} Celsius")
except ValueError as ve:
    print(f"Kesalahan Input: {ve}")
except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")
finally:
    print("Terima kasih telah menggunakan Kalkulator Konversi Suhu.")
