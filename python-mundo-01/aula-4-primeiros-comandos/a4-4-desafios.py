# ================================
#             Desafios
# ================================


# 1 - Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitato.

nome = input('Digite seu nome: ')

print('Seja bem-vindo(a), ' + nome + "!")


# 2 - Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

dia = input('Digite o dia do seu nascimento: ')
mes = input('Digite o mês do seu nascimento: ')
ano = input('Digite o ano do seu nascimento: ')

print('Você nasceu em: ' + dia + '/' + mes + '/' + ano + '.')


# 3 - Crie um script em Python que leia dois números e tente mostrar a soma entre eles.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
print(num1 + num2)