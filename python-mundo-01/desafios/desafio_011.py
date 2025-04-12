# ================================
#        Desafio 011
# ================================

# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

entrada = input('Digite a largura seguida de espaço e a altura da parede: ')

altura, largura = map(float, entrada.split())

area = altura * largura

tinta = area / 2

print(f'Área: {area:.2f} m\u00B2')
print(f'Quantidade de tinta: {tinta}')
