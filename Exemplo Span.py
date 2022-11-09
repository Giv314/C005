# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:20:17 2022
Exemplo com search, span e group
@author: giova
"""
#importando bib
import re

txt = 'O rato roeu a roupa do rei de roma. Que rato danado!'

x = re.search("r[a-z]+", txt)
print(x.span())
#No python, o primeiro argumento é inclusive e o útlimo argumento é exclusive (n conta)
# Por isso, ele mostra (2,6). 6 é exclusive, 2 é inclusive


#Mostrando todos os matches
for match in re.finditer('r[a-z]+', txt):
    print(match.span())
#Retorna duas tuplas

# Quando usamos ^$ queremos analisar o texto como um todo