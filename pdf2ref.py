import os
import PyPDF2

def extract_info_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        meta = pdf.metadata
        title = meta.title
        author = meta.author
        if not title:
            title = pdf.pages[0].extract_text().split('\n')[0].strip()
        if not author: 
            author = pdf.pages[0].extract_text().split('\n')[1].strip()
        return title, author
    
def list_paper_references(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("References"+'\n')
        files = os.listdir(folder_path)
        cnt = 0
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if file_name.endswith('.pdf'):
                title, author = extract_info_from_pdf(file_path)
                if title and author:
                    cnt += 1
                    reference = f"[{cnt}] {author}. {title}."
                    file.write(reference + '\n')

# Provide the folder path where the PDFs are located
folder_path = 'C:/Users/ss263/Desktop/thesis/FA-GAN/example'
output_file = 'C:/Users/ss263/Desktop/thesis/FA-GAN/example/output.txt'
list_paper_references(folder_path, output_file)
