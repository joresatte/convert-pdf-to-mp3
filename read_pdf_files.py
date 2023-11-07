import os, glob, PyPDF2, shutil

from pathlib import Path
path_diles_list = os.listdir(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\moved_pdf')
path= Path(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\moved_pdf')

output = []
file_path_not_in_list= []
def read_files(file_path_list):
    if file_path_list[0] not in path_diles_list:
            read_file = glob.glob(os.path.join(file_path_list[0]))
    for file in read_file:
        pdfReader = PyPDF2.PdfReader(file)
        count = len(pdfReader.pages)
        if count<250:
            for i in range(count):
                page = pdfReader.pages[i]
                output.append(page.extract_text())
    return output, True

def move_file_path(file_path_list):
    if read_files(file_path_list)==True:
            shutil.move(file_path_list[0], path)
             

        



