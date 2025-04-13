# ================================
#        Desafio 017
# ================================
# Faça um programa que leia o comprimento do cateto oposto e do cateto ajacente de um triângulo retângulo. Calcule e mostre o comprimenhto da hipotenusa.

from math import sqrt

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

quadrado_hipotenusa = cateto_oposto ** 2 + cateto_adjacente ** 2

hipotenusa = sqrt(quadrado_hipotenusa)

print(f'Hipotenusa = {hipotenusa:.2f}')

