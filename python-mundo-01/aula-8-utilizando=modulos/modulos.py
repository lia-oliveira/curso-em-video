# ================================
#            Módulos
# ================================
#import math
from math import sqrt, floor, ceil
import random

num = int(input('Digite um númeo: '))
#raiz = math.sqrt(num)
raiz = sqrt(num)
print(' A raiz de {} é igual a {}'.format(num, floor(raiz)))
print(' A raiz de {} é igual a {}'.format(num, ceil(raiz)))


num2 = random.random()
num3 = random.randint()
print(num2)
print(num3)




