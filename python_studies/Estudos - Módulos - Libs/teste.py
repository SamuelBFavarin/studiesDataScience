#Tipos de importação:
#tomar cuidado com importações globais, devido que metodos de diversos modulos podem ter o mesmo nome, causando assim problemas

#import my_math
#from my_math import area_quad
from my_math import *

#biblioteca math do python
import math

print(area_quad(5))
print(area_ret(5,10))

print(math.factorial(5))