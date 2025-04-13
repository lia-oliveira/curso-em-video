# ================================
#        Desafio 019
# ================================

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

alunos = ['Chaves','Chiquinha', 'Kiko', 'Nhonho']

aluno_sorteado = choice(alunos)

print(f'Aluno escolhido: {aluno_sorteado}')




