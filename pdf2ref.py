import os
import argparse
import PyPDF2

def extract_info_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        meta = pdf.metadata
        title = meta.title
        author = meta.author
        date = meta.creation_date if meta.creation_date else " date unknown"
        if not title:
            title = pdf.pages[0].extract_text().split('\n')[0].strip()
        if not author: 
            author = pdf.pages[0].extract_text().split('\n')[1].strip()
        return title, author, date
    
def list_paper_references(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("References"+'\n')
        files = os.listdir(folder_path)
        cnt = 0
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if file_name.endswith('.pdf'):
                title, author, date = extract_info_from_pdf(file_path)
                if title and author and date:
                    cnt += 1
                    reference = f"[{cnt}] {author}. {title}, {str(date)[:4]}"
                    file.write(reference + '\n')


parser = argparse.ArgumentParser(description="parameters for reference list generation")

parser.add_argument('-f',
                    '--folder_path',
                    help="Please enter the folder path where the research paper PDF file is located",
                    type=str,
                    required = True)

parser.add_argument('-o',
                    '--output_path',
                    help="Please enter the path where txt file with reference list will be saved",
                    type=str,
                    required=True)

args = parser.parse_args()

try:
  assert os.path.isdir(args.folder_path), "Input path does not exist"
  assert os.path.isdir(os.path.dirname(args.output_path)), 'Output path directory does not exist'
  list_paper_references(args.folder_path, args.output_path)
except AssertionError as e:
  print(str(e))
  print("Check the folder path and output path")


