import os
import comtypes.client
import shutil

curent_dir= os.chdir(r'IFAS TRABAJO SOCIAL')

arr = os.listdir(r'C:\Users\Karte\Downloads\PROYECTOS\Pdf_Doc\IFAS TRABAJO SOCIAL')

wdFormatPDF = 17

def convertFile(file):
    in_file = os.path.abspath(file)
    out_file = os.path.abspath(file.replace(".docx", ".pdf").replace(".doc", ".pdf"))
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


def convert_file_to_PDF():
    # minArgsLenght is the value that is used to find out if the user introduced file paths or not
    minArgsLength = 1
    if(len(arr)) > minArgsLength:
        for file in arr:
            if file.endswith(".doc") or file.endswith(".docx"):
                convertFile(file)
    return arr

def move_doc_file(files_list):
    for file in files_list:
        if file.endswith(".doc") or file.endswith(".docx"):
            shutil.move(file, r"C:\Users\Karte\Downloads\PROYECTOS\Pdf_Doc\docx_files")