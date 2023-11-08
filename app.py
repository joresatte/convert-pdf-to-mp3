import pyttsx3
# from gtts import gTTS
import os , glob, PyPDF2, shutil
# import get_list_path
from pathlib import Path

curent_dir= os.chdir(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\IFAS TRABAJO SOCIAL')
path= Path(r'C:\Users\jores.atte\Downloads\Proyectos personales\convert-pdf-to-mp3\moved_pdf')

def convert_file_toMp3(file_path_list):
    if file_path_list[0]:
        for i in file_path_list[0]:
            file_path= Path(r'C:\Users\Karte\Downloads\PROYECTOS\Pdf_Doc\IFAS TRABAJO SOCIAL'+'\\' + str(i))
            read_files = glob.glob(os.path.join(file_path))
    print(read_files)
    output = []
    # first_part=[]
    # second_part= []
    for files in read_files:
        pdfReader = PyPDF2.PdfReader(files)
        count = len(pdfReader.pages)
        if count<250:
            for i in range(count):
                page = pdfReader.pages[i]
                output.append(page.extract_text())
                
    seperator = ','
    newoutput = seperator.join(output).replace('\n', '')
    # first_part_output = seperator.join(output).replace('\n', '')
    # second_part_output = seperator.join(output).replace('\n', '')
    #print(newoutput)

    # Initialize the Pyttsx3 engine
    engine = pyttsx3.init()
    newVoiceRate = 145
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', 'es-es')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',newVoiceRate)
    # engine.say(newoutput)
    name, ext= os.path.splitext(file_path_list[0])
    name= name
    engine.save_to_file(newoutput, name+'.mp3')
    # Wait until above command is not finished.
    engine.runAndWait()
    if newoutput is not None and name is not None:
         shutil.move(file_path_list[0], path)
    else:
         raise Exception("Sorry, can't convert file")