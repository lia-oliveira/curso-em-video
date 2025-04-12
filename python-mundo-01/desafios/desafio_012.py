# ================================
#        Desafio 012
# ================================

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor do produto: R$ '))

preco_com_desconto = preco * 0.95

print(f"Preço com 5% de desconto: R$ {preco_com_desconto:.2f}")