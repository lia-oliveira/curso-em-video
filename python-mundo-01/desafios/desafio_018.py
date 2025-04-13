# ================================
#        Desafio 018
# ================================

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo_em_graus = int(input('Digite um ângulo em graus: '))
angulo_em_radianos = radians(angulo_em_graus)

seno = sin(angulo_em_radianos)
cosseno = cos(angulo_em_radianos)
tangente = tan(angulo_em_radianos)

print(f'Seno do ângulo de {angulo_em_graus}\u00B0: {seno:.2f}')
print(f'Cosseno do ângulo de {angulo_em_graus}\u00B0: {cosseno:.2f}')
print(f'Tangente do ângulo de {angulo_em_graus}\u00B0: {tangente:.2f}')
