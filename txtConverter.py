from gtts import gTTS


class Converter:
    def convertTxt(self, mytext):
        language= 'es'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("convert_to.mp3")

        return "start convert_to.mp3"
        


# from io import StringIO

# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfparser import PDFParser

# output_string = StringIO()
# with open('TEMARIO ADMINISTRATIVO 2023.pdf', 'rb') as in_file:
#     parser = PDFParser(in_file)
#     doc = PDFDocument(parser)
#     rsrcmgr = PDFResourceManager()
#     device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     list_text=[interpreter.process_page(page) for page in PDFPage.create_pages(doc)]
# for i in list_text:
#     if '\n' in i:
#         text= output_string.getvalue(i.replace('\n', ''))
# print(text)
# from pdfminer.high_level import extract_text_to_fp, extract_pages, extract_text
# from pdfminer.layout import LTTextContainer, LTChar, LTRect, LTFigure
# from io import StringIO
# import fitz
import pyttsx3
from PyPDF2 import PdfReader
from gtts import gTTS
import os 

# from pathlib import Path


# output_string = StringIO()
# with open('TEMARIO ADMINISTRATIVO 2023.pdf', 'rb') as fin:
#      extract_text_to_fp(fin, output_string)
# text_to_convert= output_string.getvalue().replace('\n', '')

# doc = fitz.open("TEMARIO ADMINISTRATIVO 2023.pdf")
# extrated_text= [page.get_text() for page in doc]

# print(text_to_convert)
# for page_layout in extract_text('TEMARIO ADMINISTRATIVO 2023.pdf'):
#     for element in page_layout:
#         print(element)
reader= PdfReader('TEMARIO ADMINISTRATIVO 2023.pdf')
# extrated_text= [page.extract_text() for page in reader.pages[0:7]]
# extrated_text2= [page.extract_text() for page in reader.pages[0:8]]
extrated_text3= [page.extract_text() for page in reader.pages[8:9]]
extrated_text4= [page.extract_text() for page in reader.pages[9:10]]
# extrated_text5= [page.extract_text() for page in reader.pages[0:11]]
# extrated_text6= [page.extract_text() for page in reader.pages[0:12]]
# print(extract_text)

# list_to_process=[]
# for item in extrated_text: 
#     if '\n' in item:
#         list_to_process.append(item.replace('\n',''))

# list_to_process2=[]
# for item in extrated_text2: 
#     if '\n' in item:
#         list_to_process2.append(item.replace('\n',''))

list_to_process3=[]
for item in extrated_text3: 
    if '\n' in item:
        list_to_process3.append(item.replace('\n',''))

list_to_process4=[]
for item in extrated_text4: 
    if '\n' in item:
        list_to_process4.append(item.replace('\n',''))

# list_to_process5=[]
# for item in extrated_text5: 
#     if '\n' in item:
#         list_to_process5.append(item.replace('\n',''))

# list_to_process6=[]
# for item in extrated_text6: 
#     if '\n' in item:
#         list_to_process6.append(item.replace('\n',''))
# print(list_to_process)

# # with open('text_to_convert_to_voz.txt', 'w' ) as file:
# #     file.write(" ".join(item).encode('utf8'))

# txt = Path('TEMARIO ADMINISTRATIVO 2023.txt')
# with open(txt, 'r' , encoding= 'utf-8') as file:
#     txt_file= file.readlines()
# for line in txt_file:
#     list_to_process.append(line)
# for item in list_to_process:
#     if '\n' in item:
#         text+= ''.join(item.replace('\n', ''))

# print(text)



# txt_txt = txt.replace('\n', '')
# print(txt)
# text=''
# for i in list_to_process:
#     text= ''.join(i)

# text2=''
# for i in list_to_process2:
#     text2= ''.join(i).replace('\n', '')

text3=''
for i in list_to_process3:
    text3= ''.join(i).replace('\n', '')
# print('text3',text3)

text4=''
for i in list_to_process4:
    text4= ''.join(i).replace('\n', '')

# print('text4',text4)

# text5=''
# for i in list_to_process5:
#     text5= ''.join(i)

# text6=''
# for i in list_to_process6:
#     text6= ''.join(i)
# print(text)
# Initialize the Pyttsx3 engine
engine = pyttsx3.init()
# newVoiceRate = 145
# voices = engine.getProperty('voices') 
# engine.setProperty('voice', 'es-es')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate',newVoiceRate)
# # engine.say(text)
# # engine.say(text2)
# engine.save_to_file(text, 'speech.mp3')

# # Wait until above command is not finished.
# engine.runAndWait()


# newVoiceRate = 145
# voices = engine.getProperty('voices') 
# engine.setProperty('voice', 'es-es')
# engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate',newVoiceRate)
# # engine.say(text)
# # engine.say(text2)

# engine.save_to_file(text2, 'speech2.mp3')
# # Wait until above command is not finished.
# engine.runAndWait()


newVoiceRate = 145
voices = engine.getProperty('voices') 
engine.setProperty('voice', 'es-es')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',newVoiceRate)
# engine.say(text)
# engine.say(text2)
engine.save_to_file(text3, 'speech2.mp3')
# Wait until above command is not finished.
engine.runAndWait()

newVoiceRate = 145
voices = engine.getProperty('voices') 
engine.setProperty('voice', 'es-es')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',newVoiceRate)
# engine.say(text)
# engine.say(text2)
engine.save_to_file(text4, 'speech2.mp3')
# Wait until above command is not finished.
engine.runAndWait()

# newVoiceRate = 145
# voices = engine.getProperty('voices') 
# engine.setProperty('voice', 'es-es')
# engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate',newVoiceRate)
# # engine.say(text)
# # engine.say(text2)

# engine.save_to_file(text5, 'speech2.mp3')
# # Wait until above command is not finished.
# engine.runAndWait()

# newVoiceRate = 145
# voices = engine.getProperty('voices') 
# engine.setProperty('voice', 'es-es')
# engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate',newVoiceRate)
# # engine.say(text)
# # engine.say(text2)
# engine.save_to_file(text6, 'speech2.mp3')
# # Wait until above command is not finished.
# engine.runAndWait()
# # print(text)
# # Initialize the Pyttsx3 engine
# newVoiceRate = 145
# engine.setProperty('voice', 'es-es')
# engine.setProperty('rate',newVoiceRate)
# # engine.say(text)
# engine.save_to_file(text2, 'speech2.mp3')
# # Wait until above command is not finished.
# engine.runAndWait()

# language= 'es'
# myobj = gTTS(text=text3 , lang=language, slow=False)
# myobj.save("speech3.mp3")
# os.system("start speech3.mp3"+ " tempo 3.0")

