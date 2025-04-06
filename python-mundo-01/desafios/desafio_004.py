# ================================
#        Desafio 004
# ================================

# 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

algo= input('Digite algo: ')

print(f'Você digitou: {algo}')
print(type(algo))
print('É alfabético? ', algo.isalpha())
print('É alfabético? ', algo.replace(" ", "").isalpha())  
print('É alfa-numérico? ', algo.isalnum()) 
print('É dígito? ',algo.isdigit())   
print('É apenas espaço? ',algo.isspace())
print('Coloca em maiúsculas: ',algo.upper())
print('Coloca em minúsculas: ', algo.lower())
print('O texto está em caixa altao? ', algo.isupper())
print('O texto está em caixa baixa? ', algo.islower())
print('O texto está capitalizado? ', algo.istitle())