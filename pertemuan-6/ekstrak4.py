from PIL import Image
import pytesseract
import os


# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Specify the folder path
folder_path = 'C:\\Users\\LENOVO\\OneDrive\\Documents\\ekstrak_jpg\\data'

# Get a list of all files in the folder
jpg_files = os.listdir(folder_path)

# Filter out only files (optional)
jpg_files = [f for f in jpg_files if os.path.isfile(os.path.join(folder_path, f))]

# Loop through each file 
i = 1
for file_name in jpg_files:
    jpg_filepath = os.path.join(folder_path, file_name)

    image = Image.open(jpg_filepath)
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    lines = text.splitlines()
    modified_lines = lines[8:-9]
    
    # Data Nama Mahasiswa dan NIM
    nim_nama = lines[5]    
    parts = [A.strip() for A in nim_nama.split(':')] # nim dan nama
    parts[1] = parts[1].replace('NIM', '').strip()
    nama = parts[1]
    nim = parts[2]
    
    # Data Semester, Tahun Akademik, dan Nama Prodi
    semester_prodi = lines[6]
    parts2 = [B.strip() for B in semester_prodi.split(':')] # Tahun, semester, dan Prodi
    smt = parts2[1]
    jur = parts2[2]
    semester_tahun = smt.split('-')               
    tahun_text = semester_tahun[1].split()
    semester_prodi = jur.split('-')
    prodi_text = semester_prodi[1].split()

    semester = semester_tahun[0]
    tahun = tahun_text[0]
    prodi = semester_prodi[1]

    print(f"NIM:{nim} - {nama}")
    print(f"Semester: {semester} - Tahun Akademik: {tahun} - Prodi: {prodi}")
    
    for x in modified_lines:
        print(x)

