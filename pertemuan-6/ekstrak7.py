from PIL import Image
import pytesseract
import os
import csv


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
gabungan = []
for file_name in jpg_files:
    jpg_filepath = os.path.join(folder_path, file_name)

    image = Image.open(jpg_filepath)
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    lines = text.splitlines()
    
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

    modified_lines = lines[8:-9]
    check = modified_lines[-2]
    if(check=='os'):
        modified_lines = lines[8:-12]
    else:
        modified_lines = lines[8:-9]
    #print(f"NIM:{nim} - {nama}")
    #print(f"Semester: {semester} - Tahun Akademik: {tahun} - Prodi: {prodi}")
    
    cleaned_lines = [line.replace('2,', '2').strip() for line in modified_lines]
    cleaned_lines = [line.replace('2:', '2').strip() for line in cleaned_lines]
    cleaned_lines = [line.replace('2 0', '2 E 0').strip() for line in cleaned_lines]
    cleaned_lines = [line.replace('€', 'C').strip() for line in cleaned_lines]
    cleaned_lines = [line.replace('3  C', '3 C').strip() for line in cleaned_lines] 
    cleaned_lines = [line.replace('3.', '3').strip() for line in cleaned_lines]
    cleaned_lines = [line.replace('.C', 'C').strip() for line in cleaned_lines]
    cleaned_lines = [line.replace('9  C', '9 C').strip() for line in cleaned_lines]
    
    # Remove the first two columns from cleaned_lines
    cleaned_lines = [' '.join(line.split()[2:]) for line in cleaned_lines if len(line.split()) > 2]
    cleaned_lines = [' '.join(line.split()[:-1]) for line in cleaned_lines if len(line.split()) > 1]
    
    formatted_data = []

    for entry in cleaned_lines:
        parts = entry.split()  # Split the entry into parts
        subject = " ".join(parts[:-2])  # Join all but the last two parts as the subject
        credits = int(parts[-2])  # The second last part is the credits
        grade = parts[-1]  # The last part is the grade
        print(f"NIM:{nim}, Nama:{nama}, MK:{subject}, sks:{credits}, Grade:{grade}")
        formatted_entry = f"{nim}, {nama}, {subject}, {credits}, {grade}, {semester}, {tahun}, {prodi}"  # Format the entry as a string
        formatted_data.append(formatted_entry)   
    gabungan = gabungan + formatted_data

indexed_list = [f"{index + 1}, {item}" for index, item in enumerate(gabungan)]
print("\n".join(indexed_list))

# Add index to each item
indexed_list = [[index + 1] + item.split(", ") for index, item in enumerate(gabungan)]

# Specify the header
header = ["Index", "NIM", "Nama", "Subject", "Credit", "Grade", "Semester", "Tahun", "Prodi"]

# Save to CSV file
with open('peternakan.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write header
    writer.writerows(indexed_list)  # Write data rows

print("Data has been saved to peternakan.csv")

print("Done.")