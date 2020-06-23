# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:04:33 2020

@author: jdros
"""

def retornar(lista):
    if len(lista)==1:
        return [[max(lista[0])]+[min(lista[0])]+[max(lista[0])+min(lista[0])]]
                     
    return [[max(lista[0])]+[min(lista[0])]+[max(lista[0])+min(lista[0])]] +retornar(lista[1:])

print(retornar([[1,5,33],[154,3,5],[58,7,9],[5,10,12]]))