# ================================
#        Desafio 020
# ================================

# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

alunos = ['Chaves','Chiquinha', 'Kiko', 'Nhonho']

embaralhados = alunos.copy()
shuffle(embaralhados)


print('Ordem de apresentação dos trabalhos:')
for aluno in embaralhados:
    print(aluno)