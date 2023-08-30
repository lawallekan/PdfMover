import os
import shutil

# Source and destination folders
download_folder = r"C:\Users\RAZER\Downloads"
destination_folder = r"C:\Users\RAZER\Downloads\pdfs test"

# Get a list of all files in the download folder
files = os.listdir(download_folder)

# Filter out only PDF files (you can adjust this condition as needed)
pdf_files = [file for file in files if file.lower().endswith('.pdf')]

# Move each PDF file to the destination folder
for pdf_file in pdf_files:
    source_path = os.path.join(download_folder, pdf_file)
    destination_path = os.path.join(destination_folder, pdf_file)
    
    try:
        shutil.move(source_path, destination_path)
        print(f"Moved: {pdf_file}")
    except Exception as e:
        print(f"Error moving {pdf_file}: {e}")
