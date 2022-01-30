# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:44:17 2022

@author: Matheus Mendes
"""




def tratar_string(string):
    string = remover_espacos(string)
    string = remover_pontos_e_hifens(string)
    string = remover_acentos(string)
    string = string.replace('|','I') # O OCR as vezes identifica "I" como "|"
    return string.lower()

tratar_string(string)
