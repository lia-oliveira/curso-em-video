# ================================
#        Desafio 006
# ================================

# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

num = input('Digite um número: ')

if (type(num) == int):
    num = int(num)

if (type((num) == float)):
    num = float(num)


dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** (1/2)

print('Número:', num)
print('Dobro:', dobro)
print('Triplo:', triplo)
print(f'Raiz quadrada: {raiz_quadrada:.2f}')
