# ================================
#        Desafio 009
# ================================

# Faça um programa que leia um números inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número inteiro entre 1 e 9: '))

if 1 <= num <= 9:
    for i in range(1,11):
        print(f'{num} x {i} = {num * i}')