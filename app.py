import pyttsx3
# from gtts import gTTS
import os , glob, PyPDF2, sys

curent_dir= os.chdir(r'IFAS TRABAJO SOCIAL')

file_path= r'C:\Users\Karte\Downloads\PROYECTOS\Pdf_Doc\IFAS TRABAJO SOCIAL\16- Decreto foral 117.2022.pdf'
read_files = glob.glob(os.path.join(file_path))
print(read_files)
output = []
# first_part=[]
# second_part= []
for files in read_files:
    pdfReader = PyPDF2.PdfReader(files)
    count = len(pdfReader.pages)
    output = []
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
# newVoiceRate = 145
# voices = engine.getProperty('voices') 
# engine.setProperty('voice', 'es-es')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate',newVoiceRate)
# # engine.say(newoutput)
# engine.save_to_file(newoutput, 'speech.mp3')
# # Wait until above command is not finished.
# engine.runAndWait()
newVoiceRate = 145
voices = engine.getProperty('voices') 
engine.setProperty('voice', 'es-es')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',newVoiceRate)
# engine.say(newoutput)
engine.save_to_file(newoutput, 'fourteenthspeech.mp3')
# Wait until above command is not finished.
engine.runAndWait()
