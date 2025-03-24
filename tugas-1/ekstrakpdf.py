import pdfplumber
import pandas as pd

# Fungsi untuk mengekstrak teks dari PDF
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Fungsi untuk mengekstrak tabel dari PDF
def extract_table_from_pdf(pdf_path):
    all_data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            table = page.extract_table()
            if table:
                all_data.extend(table[1:])  # Menyimpan hanya data, tanpa header
    return all_data

# Fungsi untuk menyimpan data teks dan tabel ke CSV
def save_to_csv_with_text_and_table(text_data, table_data, output_csv):
    # Gabungkan teks dan tabel dalam satu CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = pd.ExcelWriter(f)
        
        # Menulis teks di bagian awal file CSV
        f.write(f"Teks yang diekstrak dari PDF:\n{text_data}\n\n")
        
        # Menulis tabel setelah teks
        if table_data:
            df = pd.DataFrame(table_data, columns=["No", "NIM", "Nama", "Kehadiran", "UTS", "UAS", "Sikap", 
                                                   "Tugas Harian", "Tugas Kelompok", "Tugas Besar", "Nilai Akhir", "Nilai Mutu"])
            df.to_csv(f, index=False)

# Fungsi utama untuk memproses 5 file PDF terpisah dan menyimpannya sebagai CSV terpisah
def main():
    # List file PDF yang ingin diproses
    pdf_files = [
        "Ganjil_2022_Aljabar Linier Matriks_Kelas_A.pdf",
        "Ganjil_2022_Bahasa Indonesia_Kelas_A.pdf",
        "Ganjil_2022_Bahasa Inggris_Kelas_A.pdf",
        "Ganjil_2022_Dasar-dasar Pemasaran_Kelas_A.pdf",
        "Ganjil_2022_Fisika Dasar_Kelas_A.pdf"
    ]
    
    # Proses setiap file PDF
    for pdf_file in pdf_files:
        print(f"Membaca file: {pdf_file}")
        
        # Ekstrak teks dan tabel dari PDF
        text_data = extract_text_from_pdf(pdf_file)
        table_data = extract_table_from_pdf(pdf_file)
        
        # Tentukan nama file CSV yang sesuai berdasarkan nama file PDF
        output_csv = pdf_file.replace(".pdf", "_with_text_and_table.csv")
        
        # Simpan data teks dan tabel ke CSV terpisah
        if table_data:  # Jika ada data tabel
            save_to_csv_with_text_and_table(text_data, table_data, output_csv)
            print(f"Teks dan tabel berhasil disimpan di {output_csv}")
        else:
            print(f"Tidak ada data untuk disimpan di {output_csv}")

if __name__ == "__main__":
    main()
