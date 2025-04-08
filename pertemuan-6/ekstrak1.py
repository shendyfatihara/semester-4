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


    # Load the image
    image = Image.open(jpg_filepath)
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    lines = text.splitlines()
    for row in lines:
        print(row)
