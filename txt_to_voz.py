import get_list_path, read_pdf_files
import app


    
def get_MP3():
    list_to_read= get_list_path.convert_file_to_PDF()
    print(list_to_read)
    pdf_list_file_path= get_list_path.move_doc_file(list_to_read)
    print(pdf_list_file_path)
    if pdf_list_file_path == 'Successfully':
        read_pdf_files.read_files()
    return 'very good'
        

# def convert_to_MP3(string_output):
#     string_output= get_string()
#     # Initialize the Pyttsx3 engine
#     engine = pyttsx3.init()
#     newVoiceRate = 145
#     voices = engine.getProperty('voices') 
#     engine.setProperty('voice', 'es-es')
#     engine.setProperty('voice', voices[0].id)
#     engine.setProperty('rate',newVoiceRate)
#     engine.save_to_file(string_output, 'speech.mp3')
#     # Wait until above command is not finished.
#     engine.runAndWait()


string_to_covert= get_MP3()
print(string_to_covert)
# convert_to_MP3(string_to_covert)