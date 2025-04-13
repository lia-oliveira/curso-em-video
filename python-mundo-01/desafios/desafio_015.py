# ================================
#        Desafio 015
# ================================

# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

km_percorrido = float(input('Digite a quilopetragem percorrida: '))
dias = int(input('Foi alugado por quantos dias? '))

aluguel = 60.0 * dias
preco_por_km = km_percorrido * 0.15
total = aluguel + preco_por_km

print(f'Total a pagar: R$ {total:.2f}')