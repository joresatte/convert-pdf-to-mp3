import get_list_path, read_pdf_files
import app, os
from pathlib import Path
current_dir= os.getcwd()
path = Path(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\docx_files')
path_string = Path(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\IFAS TRABAJO SOCIAL')
mp3_dir= Path(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\mp3')
path_deleted_list = os.listdir(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\moved_pdf')
path_mv= Path(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\moved_pdf')

def get_MP3():
    moved_mp3_file= get_list_path.move_mp3_file_path(path_string, mp3_dir)
    print(moved_mp3_file)
    list_to_read= get_list_path.convert_file_to_PDF(path_string)
    # print('list to convert to pdf:', list_to_read)
    pdf_list_file_path= get_list_path.move_doc_file(list_to_read, path)
    # print('file path moved', pdf_list_file_path)
    if pdf_list_file_path == 'Successfully':
        get_string= read_pdf_files.read_files(list_to_read, path_deleted_list)
        if get_string== 'Done':
            return 'very good'
    if pdf_list_file_path== 'Only Pdf files':
        get_string= read_pdf_files.read_files(list_to_read, path_deleted_list)
        if get_string== 'Done':
            return 'very good'
    
def moved_converted_file(check_string):
    if get_MP3()== check_string:
        ended_process= read_pdf_files.move_file_path(path_string, path_mv)
    return ended_process

string_to_covert= get_MP3()
end_process= moved_converted_file('very good')
print(string_to_covert)
print(end_process)