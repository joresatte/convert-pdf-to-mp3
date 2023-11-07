import os, glob, PyPDF2
curent_dir= os.chdir(r'IFAS TRABAJO SOCIAL')
arr = os.listdir(r'C:\Users\Karte\Downloads\PROYECTOS\Pdf_Doc\IFAS TRABAJO SOCIAL')

file_path_range=0
output = []
file_path_not_in_list= []
def read_files(file_path_list):
    for file_path in range(len(file_path_list)):
        if file_path_list[file_path] not in file_path_not_in_list:
            file_path_not_in_list.append(file_path_list[file_path])
            read_file = glob.glob(os.path.join(file_path_list[file_path]))
        else:
            continue
        for file in read_file:
            pdfReader = PyPDF2.PdfReader(file)
            count = len(pdfReader.pages)
            if count<250:
                for i in range(count):
                    page = pdfReader.pages[i]
                    output.append(page.extract_text())
            
         
    return output



