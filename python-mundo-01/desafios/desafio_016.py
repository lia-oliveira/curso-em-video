# ================================
#        Desafio 016
# ================================

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

from math import trunc

numero = float(input('Digite um número com casas decimais: '))
inteiro = trunc(numero)

print(f'O número {numero} tem a parte inteira {inteiro}.')