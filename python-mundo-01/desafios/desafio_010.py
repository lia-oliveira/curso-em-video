# ================================
#        Desafio 010
# ================================

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere USD1.00 = R$3.27

valor = float(input('Digite um valor: R$ '))


reais_para_dolar = valor / 3.27

print(f'Com {valor:.2f} BRL você pode comprar {reais_para_dolar:.2f} USD.')



