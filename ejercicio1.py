# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:41:25 2020

@author: jdros
"""

def dividir(numero):
  return  [int(i) for i in str(numero)]

def separar(lista):
  if len(lista)==1:
    return str(dividir(lista[0])[-1])
  return str(dividir(lista[0])[-1]) + separar(lista[1:])


print(separar([27,3954,4,2,1]))