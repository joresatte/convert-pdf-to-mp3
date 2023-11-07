import os
import comtypes
import shutil
from pathlib import Path
curent_dir= os.chdir(r'IFAS TRABAJO SOCIAL')

arr = os.listdir(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\IFAS TRABAJO SOCIAL')
path = Path(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\docx_files')
wdFormatPDF = 17

def convertFile(file):
    in_file = os.path.abspath(file)
    out_file = os.path.abspath(file.replace(".docx", ".pdf").replace(".doc", ".pdf"))
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Add(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


def convert_file_to_PDF():
    if arr is not None:
        for file in arr:
            if file.endswith(".doc") or file.endswith(".docx"):
                convertFile(file)
    return arr

def move_doc_file(files_list):
    for file in files_list:
        if file.endswith(".doc") or file.endswith(".docx"):
            shutil.move(file, path)