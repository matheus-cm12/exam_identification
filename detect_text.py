# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:44:17 2022

@author: Matheus Mendes
"""


from unicodedata import normalize
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def detect_text(path):

    #get credentials
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\Beep Saude\OneDrive\Documentos\Python Scripts\Keys\cvision-329618-dee6c766bc4d.json" 

    #get the OCR to
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()
    
    #open and read the file
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)    
    response = client.text_detection(image=image)
    texts = response.text_annotations    
    
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    #return only the text    
    try:
        extracted_text = texts[0].description
    except:
        extracted_text = 'N/A'
    return extracted_text

     
index = 2
texto = []

    
# for index in range(1,5):
path = r"C:\Users\Beep Saude\OneDrive\Área de Trabalho\Teste OCR\teste " + str(index) +".jpg"

string = detect_text(path) + " Tireoestimulante" + " absdtsaqyzabc" + " TSH - Hormonio" +" eas" + " EAS"

teste = ["urina",'tsa','EAS','hemograma','snp / cgh / array','culturaa','easmo','qyz','TSH - Hormonio Tireoestimulante']

teste = teste.lower()
string = string.lower()

# string = tratar_string(string)
# teste = tratar_string(teste)

fuzzratio=[]
fuzzpartialratio=[]
fuzztoken = []
fuzztokenset =[] 

for i in range(0,len(teste)):
    print(str(fuzz.token_set_ratio(string , teste[i]))+' '+str(i)+' '+teste[i])
    i=i+1
    
for i in teste:
    print(str(process.extract(i, string, limit=2, scorer=fuzz.token_set_ratio))+' '+i)


    
    fuzzratio.append(fuzz.ratio(string , teste[i]))
    fuzzpartialratio.append(fuzz.partial_ratio(string , teste[i]))
    fuzztoken.append(fuzz.token_sort_ratio(string , teste[i]))
    fuzztokenset.append(fuzz.token_set_ratio(string, teste[i]))


string = var[0].description

def remover_espacos(string):
    return ''.join(string.split())

def remover_pontos_e_hifens(string):
    string = string.replace('-','')
    return string.replace('.','')

def remover_acentos(string):
    string_sem_acentos = normalize('NFKD', string).encode('ASCII','ignore').decode('ASCII')
    return(string_sem_acentos)

def tratar_string(string):
    string = remover_espacos(string)
    string = remover_pontos_e_hifens(string)
    string = remover_acentos(string)
    string = string.replace('|','I') # O OCR as vezes identifica "I" como "|"
    return string.lower()

tratar_string(string)
