class KalkulatorPersentase:

    @staticmethod
    def hitung_persen(nilai, persen):
        return (nilai * persen) / 100

try:
    nilai = float(input("Masukkan nilai: "))
    persen = float(input("Masukkan persentase: "))
    
    hasil = KalkulatorPersentase.hitung_persen(nilai, persen)
    print(f"{persen}% dari {nilai} adalah {hasil}")

except ValueError as ve:
    print(f"Kesalahan Input: {ve}")

except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")

finally:
    print("Terima kasih telah menggunakan Kalkulator Persentase.")