# ---------------------------------------------
#            Aula 10 - Condicionais
# ---------------------------------------------

tempo = int(input('Quanto anos tem seu carro? '))

# Condicional Simples
if tempo == 0:
    print('Você não tem carro.')


# Condicional composta
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
    
# A condição será sempre executada    
if True:
    print('Seu carro tem {} ano(s).'.format(tempo))
    
    
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2) / 2
print('A sua média foi {}:.2f'.format(n))

# Condicional simplificada
print('Parabéns!' if n >=5 else 'Estude mais!')