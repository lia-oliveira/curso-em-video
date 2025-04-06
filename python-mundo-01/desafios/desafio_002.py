# ================================
#         Desafio 002
# ================================

# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Qual o seu nome? ')
nome2 = input('Qual o nome do seu acompanhante? ')
idades = [15, 22, 25, 28]

# Concatenando Strings e variáveis
print('Seja bem-vindo(a) ' + nome + '!')

# Método format - argumentos posicionais
# As variáveis dentro do format() devem estar na ordem em que aparecem no print.
# Que bom que você veio Maria!
print('Que bom que você veio {}!'.format(nome))

# Método format - argumentos nomeados
# Que bom que vocês vieram Maria e João!
print('Que bom que vocês vieram {convidado} e {acompanhante}!'.format(convidado=nome, acompanhante=nome2))

# F-Strings
# Maria, bom te ver por aqui!
print(f'{nome}, bom te ver por aqui!')

# end acrescenta um caracter ou espaço ao final da string de acordo com o que for determinado.
# Se o end não estivesse no primeiro print as frases teriam sido exibidas em linhas diferentes.
# Maria e João - Aproveite(m) o evento.
print(f'{nome} e {nome2}', end=' - ')
print('Aproveite(m) o evento.')

# Separador
# Jordana | Lucas | Rafaela | Marcos
print('Quem ainda não chegou?')
print('Jordana', 'Lucas', 'Rafaela', 'Marcos', sep=' | ')

# Impressão com *
# 15 22 25 28
print(*idades)