print('5 + 3 * 2 = ',5 + 3 * 2)

print('5**2 = ', 5**2)

print('5**3 = ', 5**3)

print('19 // 2= ', 19 // 2)

print('18 % 2 =', 18 % 2 )

print('122 % 3 =', 122 % 3 )

print('4 ** 3 =', 4 ** 3 )
print(pow(4,3))

print('Raíz quadrada de 81 = ', 81 ** (1/2))
print('Raíz quadrada de 25 = ', 25 ** (1/2))
print('Raíz cúbica de 127 = ', 127 ** (1/3))

print('Oi ' * 5)

nome = input('Qual é o seu nome? ')
print(f'Prazer em te conhecer, {nome}!')
print(f'Prazer em te conhecer, {nome:>20}!')
print(f'Prazer em te conhecer, {nome:^20}!')
print(f'Prazer em te conhecer, {nome:<20}!')
print(f'Prazer em te conhecer, {nome:=^20}!')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_exata = n1 // n2
exponenciacao = n1 ** n2

print('{} + {} = {}'.format(n1, n2, soma))
print('{} - {} = {}'.format(n1, n2, subtracao))
print('{} * {} = {}'.format(n1, n2, multiplicacao))
print('{} / {} = {}'.format(n1, n2, divisao))
print('{} // {} = {}'.format(n1, n2, divisao_exata))
print('{} ** {} = {}'.format(n1, n2, exponenciacao))

# Limitando o número de casas decimais do resultado
print(f'{4 / 3:.3f}')

# Imprimir na mesma linha
print('Primeira Linha', end=' ')
print('Segunda linha')


