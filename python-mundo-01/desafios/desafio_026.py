# ================================
#        Desafio 026
# ================================

# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela apárece a primeira vez
# Em que posição ela aparece a última vez.

palavra = input('Digite uma palavra: ')

if palavra.isdigit():
    print('Palavra inválida.')
else:
    p_lower = palavra.lower()
    primero_a= p_lower.find('a')
    ultimo_a = p_lower.rfind('a')
    print(f'Posição do primeiro a: {primero_a} \nPosição do último a: {ultimo_a}')
   

