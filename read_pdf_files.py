import os, glob, PyPDF2, shutil, pyttsx3

output = []
file_path_not_in_list= []
def read_files(arr, path_deleted_list):
    try:
        for i in arr:
            if i == arr[0] and not i in path_deleted_list:
                print(arr[0], i)
                read_file = glob.glob(os.path.abspath(os.path.join(i)))     
        for file in read_file:
            pdfReader = PyPDF2.PdfReader(file)
            count = len(pdfReader.pages)
            if count<250:
                for i in range(count):
                    page = pdfReader.pages[i]
                    output.append(page.extract_text())
        seperator = ','
        newoutput = seperator.join(output).replace('\n', '')
        # print(newoutput)

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
        engine.save_to_file(newoutput, name+'.mp3')
        # Wait until above command is not finished.
        engine.runAndWait()
        engine.stop()
        if newoutput !='' and name !='':
            return 'Done'
        else:
             raise Exception("Sorry, can't convert file")
    except OSError as e:
        print("file Error: {}".format(e))


def move_file_path(path_string, path_mv):
    list_dir= os.listdir(path_string)
    shutil.move(list_dir[0], path_mv)
    return 'Ended process'
             

        



