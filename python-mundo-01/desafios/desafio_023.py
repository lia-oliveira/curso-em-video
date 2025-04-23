# ================================
#        Desafio 023
# ================================

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

n = int(input('Digite um número ente e 9999: '))
n_str = str(n)
medida = ['Unidade', 'Dezena', 'Centena', 'Milhar']

if n > 0 and len(n_str) < 5:
   for i in range(len(n_str)):
       n_inv = n_str[::-1]
       print(f'{medida[i]} = {n_inv[i]}' )
else:
    print('Número inválido.')    
    

 
    
    