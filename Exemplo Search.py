# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 21:42:08 2022

@author: giova
"""

# Importando biblioteca do regex
import re


#Variavel que guarda um texto (String)
texto = 'Os melhores engenheiros são da Argentina'

# Procurando se o padrão é atendido
x = re.search("^Os.*Brasil$", texto)
#.* siginifica infinitas repetições de qualquer coisa


#Verificando se encontrou o padrão
if x:
    print("Deu match")
else:
    print("Não deu match")
    
# A funcao search retorna objeto! Caso o objeto seja nulo, não há match