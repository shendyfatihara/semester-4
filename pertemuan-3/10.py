class KonversiJarak:
    @staticmethod
    def km_ke_mil(km):
        if km < 0:
            raise ValueError("Jarak tidak boleh negatif.")
        return km * 0.621371

try:
    km = float(input("Masukkan jarak dalam kilometer: "))
    mil = KonversiJarak.km_ke_mil(km)
    print(f"{km} kilometer = {mil:.2f} mil")
except ValueError as ve:
    print(f"Kesalahan Input: {ve}")
except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")
finally:
    print("Terima kasih telah menggunakan Kalkulator Konversi Jarak.")
