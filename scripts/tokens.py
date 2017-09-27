#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-
#
#  tokens.py
#  
#  Copyright 2013 Abel Meneses Abad <abelma1980@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
  
import queue
from queue import Queue

def ngram_index(text,n):
   """Long code for the divition given n the n-grams list of a text."""
   tokens1 = []
   for word in text.split():
      tokens1.append(word)
   m = len(tokens1)
   #inicializar la lista de ngrams
   ngram = []
   for i in range(m-n+1):
      ngram += ['']
   i,j = 0,0
   cola = queue.Queue()
   #Generar los ngrams
   for word in text.split():  #para cada palabra en el texto
      cola.put(len(word))  #Se introduce en la cola un objeto = longitud de la palabra
      word_space = ' ' + word #se adiciona un espacio en blanco a cada palabra
      ngram[i] = ngram[i] + word_space #se adiciona al elemento i del ngram la palabra en curso
      j += 1         #Contar palabras analizadas

      if i > (m-n-1):      #Si llegas a la (n-1)-última palabra salir. (solo quedarían n-1 palabras restantes que no pueden conformar un n-gram) 
         break

      elif i < (m-n) and j == n: #si se ha llegado a n palabras analizadas
         i+= 1    #Incrementar i para comenzar el ngram siguiente
         top = cola.get()#Buscar el primer elemento de la cola o sea la longitud de la primera palabra del ngram anterior
         ngram[i] = ngram[i-1][top+1:] #Construir el ngram siguiente eliminando del string la cantidad de caracteres correspondiente a la primera palabra
         j -= 1      #se disminuye en 1 a j para lograr que solo se adicione al ngram siguiente la próxima palabra del texto.

      else:
         pass     #en cualquier caso que no se haya llegado a n palabras analizadas sigue adelante con la siguiente palabra
   return ngram
