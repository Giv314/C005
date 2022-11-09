# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:09:06 2022
Exemplo com split
@author: giova
"""

import re
# Texto para realizarmos o teste
txt = "Eu gosto de sorvete de chocolate; meu pai, de creme; meu irmão, de morango"
# Quebra (splits) o texto a cada ; encontrado
x = re.split(";", txt)
print(x)
# Quebra (splits) o texto a cada espaço encontrado