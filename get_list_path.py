import os
import comtypes
import shutil
from pathlib import Path
from comtypes.client import CreateObject

wdFormatPDF = 17

def convertFile(file):
    in_file = os.path.abspath(file)
    out_file = os.path.abspath(file.replace(".docx", ".pdf").replace(".doc", ".pdf"))
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Add(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


def convert_file_to_PDF(path_string):
    pdf_list=[]
    if path_string !='':
        for file in  os.listdir(path_string):
            if (file).endswith(".doc") or (file).endswith(".docx"):
                convertFile(os.path.isfile(file))
                pdf_list.append(os.path.abspath(os.path.join(file)))
            if (file).endswith('.pdf'):
                pdf_list.append((file)) 
    return pdf_list

def move_doc_file(files_list, path):
    for file in files_list:
        if file.endswith(".doc") or file.endswith(".docx"):
            shutil.move(os.path.abspath(os.path.join(file)), path)
            return 'Successfully'
        if file.endswith('.pdf'):
            return 'Only Pdf files'
        else:
            return 'Nothing to return'
        
def move_mp3_file_path(path_string, mp3_dir):
    if path_string !='':
        for file in  os.listdir(path_string):
            if (file).endswith('.mp3'):
                shutil.move((file), mp3_dir)
                return 'Mp3 file moved'
            else:
                return 'No mp3 file'
    