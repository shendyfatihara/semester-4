import pdfplumber
import pandas as pd

def extract_table_from_pdf(pdf_path):
    all_data = []

    # Membuka file PDF
    with pdfplumber.open(pdf_path) as pdf:
        # Mengekstrak tabel dari setiap halaman
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            table = page.extract_table()

            # Mengecek apakah tabel berhasil diekstrak
            if table:
                print(f"Tabel yang diekstrak dari halaman {page_num + 1}:")
                for row in table:
                    print(row)  # Menampilkan baris tabel yang diekstrak
                all_data.extend(table[1:])  # Mengambil data tabel tanpa header
            else:
                print(f"Tabel tidak ditemukan di halaman {page_num + 1}")
    
    return all_data

def save_to_csv(data, output_csv):
    if data:
        # Menyimpan data ke CSV
        df = pd.DataFrame(data, columns=["No", "NIM", "Nama", "Kehadiran", "UTS", "UAS", "Sikap", 
                                         "Tugas Harian", "Tugas Kelompok", "Tugas Besar", "Nilai Akhir", "Nilai Mutu"])
        df.to_csv(output_csv, index=False)
        print(f"Data berhasil disimpan di {output_csv}")
    else:
        print("Tidak ada data untuk disimpan.")

def main():
    pdf_files = [
        "Ganjil_2022_Aljabar Linier Matriks_Kelas_A.pdf",
        "Ganjil_2022_Bahasa Indonesia_Kelas_A.pdf",
        "Ganjil_2022_Bahasa Inggris_Kelas_A.pdf",
        "Ganjil_2022_Dasar-dasar Pemasaran_Kelas_A.pdf",
        "Ganjil_2022_Fisika Dasar_Kelas_A.pdf"
    ]
    
    for pdf_file in pdf_files:
        print(f"\nMembaca file: {pdf_file}")
        data = extract_table_from_pdf(pdf_file)  # Ekstrak tabel dari PDF
        if data:
            output_csv = pdf_file.replace(".pdf", ".csv")
            save_to_csv(data, output_csv)  # Simpan data ke file CSV
        else:
            print(f"Tidak ada data untuk disimpan di {pdf_file.replace('.pdf', '.csv')}")

if __name__ == "__main__":
    main()
