import os, glob, PyPDF2, shutil, pyttsx3
from warnings import catch_warnings

from pathlib import Path
path_diles_list = os.listdir(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\moved_pdf')
path= Path(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\moved_pdf')
arr = os.listdir(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\IFAS TRABAJO SOCIAL')
output = []
file_path_not_in_list= []
def read_files():
    try:
        if arr[0] not in path_diles_list:
                read_file = glob.glob(os.path.abspath(os.path.join(os.path(arr[0]))))     
        for file in read_file:
            pdfReader = PyPDF2.PdfReader(file)
            count = len(pdfReader.pages)
            if count<250:
                for i in range(count):
                    page = pdfReader.pages[i]
                    output.append(page.extract_text())
        seperator = ','
        newoutput = seperator.join(output).replace('\n', '')
        print(newoutput)

        # Initialize the Pyttsx3 engine
        # engine = pyttsx3.init()
        # newVoiceRate = 145
        # voices = engine.getProperty('voices') 
        # engine.setProperty('voice', 'es-es')
        # engine.setProperty('voice', voices[0].id)
        # engine.setProperty('rate',newVoiceRate)
        # # engine.say(newoutput)
        # name, ext= os.path.splitext(file_path_list[0])
        # name= name
        # engine.save_to_file(newoutput, name+'.mp3')
        # # Wait until above command is not finished.
        # engine.runAndWait()
        # # if newoutput is not None and name is not None:
        # #      shutil.move(os.path.abspath(file_path_list[0]), path)
        # # else:
        # #      raise Exception("Sorry, can't convert file")
        return 'Done'
    except OSError as e:
        print("file Error: {}".format(e))


def move_file_path():
    if read_files()=='Done':
            shutil.move(arr[0], path)
             

        



