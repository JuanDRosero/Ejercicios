# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:15:04 2020

@author: jdros
"""

class Nodo():
    def __init__(self,valor,izquierda=None,derecha=None):
        self.valor=valor
        self.izquierda=izquierda
        self.derecha=derecha
        
def dividir(numero):
  return  [int(i) for i in str(numero)]

def dividirArbol(lista):
    if len(lista)==2:
        return [dividir(lista[0])]+[dividir(lista[1])]
    return [dividir(lista[0])]+[dividir(lista[1])]+dividirArbol(lista[2:])

def imprimirIn(arbol):
    if arbol== None:
        return []
    else:
        return imprimirIn(arbol.izquierda)+[arbol.valor]+imprimirIn(arbol.derecha)
     
    
print(dividirArbol(imprimirIn(Nodo(15,Nodo(10,derecha=Nodo(12)),Nodo(25)))))