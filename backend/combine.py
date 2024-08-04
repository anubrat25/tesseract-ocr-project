import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def combine_text_from_pdfs(pdf_folder, output_file):
    combined_text = ''
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            combined_text += extract_text_from_pdf(pdf_path) + '\n'
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(combined_text)

# Usage example
pdf_folder = r'C:\\Users\\vedant raikar\\Desktop\\ocr health project\\tesseract-ocr-project\\FDA approved'  
output_file = r"C:\Users\vedant raikar\Desktop\ocr health project\tesseract-ocr-project\FDA approved\FDADATA.txt"  # Replace with the desired output TXT file name
combine_text_from_pdfs(pdf_folder, output_file)