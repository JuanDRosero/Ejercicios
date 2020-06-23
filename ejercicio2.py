# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:43:24 2020

@author: jdros
"""

def dividir(numero):
    return [int(i) for i in str(numero)]

def multiplos(lista):
    if len(lista)==1:
        return [[3*i for i in dividir(lista[0])]]
    
    return  [[3*i for i in dividir(lista[0])]] + multiplos(lista[1:])

print(multiplos([133,254,3,154,10,33]))