# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:08:35 2022

@author: giova
"""

#importando bib
import re

#Frase
txt = 'oi! Teu pai tem boi? Foi o que pensei'
# Procurando padrões que obedem ao regex
x = re.findall('oi', txt)


#Colchetes no python são listas (array), x é um array com 3 posições
print(x)
#Comprimento do x, mostra quantos ois foram encontrados
print('Comprimento:', len(x))
