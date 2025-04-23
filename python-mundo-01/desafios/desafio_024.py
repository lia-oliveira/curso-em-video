# ================================
#        Desafio 024
# ================================

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input('Digite o nome de uma cidade: ')

if (cidade.isdigit()):
    print('Digite um nome de cidade válido.')
else:
    lista = cidade.split()
    nome = lista[0].capitalize()
    conclusao = 'Nome começa com Santo.' if nome == 'Santo' else 'O nome da cidade não começa com Santo.' 
    print(conclusao)

