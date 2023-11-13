from hashlib import new
import os, glob, PyPDF2, shutil, pyttsx3,shutil, get_list_path

output = []
file_path_not_in_list= []
def read_files(arr, path_moved_pdf):
    
    try:
        #moved_pdf_path= moved_pdf_(path_moved_pdf)
        #print(moved_pdf_path)
        for i in arr:
            if i == arr[0]:
                print(arr[0])
                read_file = glob.glob(os.path.abspath(os.path.join(i)))     
        for file in read_file:
            pdfReader = PyPDF2.PdfReader(file)
            count = len(pdfReader.pages)
            for i in range(count):
                    page = pdfReader.pages[i]
                    output.append(page.extract_text())          
        seperator = ','
        newoutput = seperator.join(output).replace('\n', '')
        newoutput.strip()
        print(len(newoutput))
        return newoutput
    except OSError as e:
        print("file Error: {}".format(e))


def move_file_path(path_string, path, path_mv):
    list_dir= os.listdir(path_string)
    list_path= os.listdir(path)
    for i in list_dir:
        for j in list_path:
            name, ext= os.path.splitext(i)
            name_, ext= os.path.splitext(j)
            if name== name_:
                shutil.move(i, path_mv)
                return 'Ended process'
             
def moved_pdf_(path_mv):
    return str(path_mv)
 
def convert_string(arr, string):
    try:
        if string!='':
            # Initialize the Pyttsx3 engine
            engine = pyttsx3.init()
            newVoiceRate = 145
            voices = engine.getProperty('voices') 
            engine.setProperty('voice', 'es-es')
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate',newVoiceRate)
            #engine.say(newoutput)
            name, ext= os.path.splitext(arr[0])
            name= name
            engine.save_to_file(string, name+'.mp3')
            # Wait until above command is not finished.
            engine.runAndWait()
            engine.stop()
            return 'file converted to mp3'
    except:
        raise Exception("Sorry, can't convert file")
    
def move_mp3_to_dir(mp3_file, mp3_dir_path):
    shutil.move(mp3_file, mp3_dir_path)
    return 'very good'

def convert_first_string(arr, first_string):
    try:
        if first_string!='':
            # Initialize the Pyttsx3 engine
            engine = pyttsx3.init()
            newVoiceRate = 145
            voices = engine.getProperty('voices') 
            engine.setProperty('voice', 'es-es')
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate',newVoiceRate)
            #engine.say(newoutput)
            name, ext= os.path.splitext(arr[0])
            name= name
            engine.save_to_file(first_string, name+'_1'+'.mp3')
            # Wait until above command is not finished.
            engine.runAndWait()
            engine.stop()
            return 'first_string converted to mp3'
    except:
        raise Exception("Sorry, can't convert file")
    
def convert_second_string(arr, second_string):
    try:
        if second_string!='':
            # Initialize the Pyttsx3 engine
            engine = pyttsx3.init()
            newVoiceRate = 145
            voices = engine.getProperty('voices') 
            engine.setProperty('voice', 'es-es')
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate',newVoiceRate)
            #engine.say(newoutput)
            name, ext= os.path.splitext(arr[0])
            name= name
            engine.save_to_file(second_string, name+'_2'+'.mp3')
            # Wait until above command is not finished.
            engine.runAndWait()
            engine.stop()
            return 'second_string converted to mp3'
    except:
        raise Exception("Sorry, can't convert file")