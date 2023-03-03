# 1 собвственные/встроенные
# 2 свои модули
# 3 внешние модули-зависимости

# venv - виртуально окружение
# она предназначена для того чтобы скачать, ограничивать и
# хранить там зависимости

import random
# import math
#
# print(math.pi)
#
# from math import e,tau
#
# print(e,tau)

# from math import *
#
# print(pi,e,tau)

# from math import pi as r
# # pi = r
# print(r)

from lesson2 import *

f = C('beka',19,'Dzy')
print(f.name)

from lesson2 import b
print(b.name)

import colorama

print(colorama.Back.BLACK)
print('синий')
print(colorama.Fore.RED)
print('красный')
print('trfygvbh')