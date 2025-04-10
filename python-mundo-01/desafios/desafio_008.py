# ================================
#        Desafio 008
# ================================


# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

valor = int(input('Digite um valor em metros: '))


metro_para_cm = valor * 100
metro_para_mm = valor * 1000


print(f'Valor em cm: {metro_para_cm}cm.')
print(f'Valor em mm: {metro_para_mm}mm.')