# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:44:17 2022

@author: Matheus Mendes
"""

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

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

