import get_list_path, read_pdf_files, os, pyttsx3


def process_list_lenght(output_list):
    if output_list is not None:
        # first_part_output= seperator.join(output_list).replace('\n', '')
        # return first_part_output
        print(output_list)

    
def get_string():
    list_to_read= get_list_path.convert_file_to_PDF()
    pdf_list_file_path= get_list_path.move_doc_file(list_to_read)
    read_list_file= read_pdf_files.read_files(list_to_read)
    string_output= process_list_lenght(read_list_file)
    if read_list_file!= None:
        read_pdf_files.move_file_path(list_to_read)
        print(string_output) 

def convert_to_MP3(string_output):
    string_output= get_string()
    # Initialize the Pyttsx3 engine
    engine = pyttsx3.init()
    newVoiceRate = 145
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', 'es-es')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',newVoiceRate)
    engine.save_to_file(string_output, 'speech.mp3')
    # Wait until above command is not finished.
    engine.runAndWait()


string_to_covert= get_string()
print(string_to_covert)
# convert_to_MP3(string_to_covert)