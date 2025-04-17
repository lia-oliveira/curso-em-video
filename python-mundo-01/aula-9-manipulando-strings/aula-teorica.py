# ================================
#     MManipulação de Strings
# ================================

# Python é case sensitive

frase = 'Curso em Vídeo Python'

frase2 = '   Aprenda Python  '

# Imprime a string inteira
print(f'\n{frase}\n')

# Imprime os caracteres com seu respectivo índice
for i, letra in enumerate(frase):
    print(f'{i} - {letra}')

# Imprime o caractere que ocupa a posição 9
print(f'Caractere na posição 9: {frase[9]}')

# Slice - pega do range do índice 9 ao 12
print(f'Range 9-12: {frase[9:13]}')

# Slice que salta de 2 em 2
print(f'Range 9-21:2: {frase[9:21:2]}')

# Slice com início omitido começa em 0
# Começa em 0 e vai até 4. Não conta o último caractere.
print(f'Range [:5]: {frase[:5]}')

# Slice começa no índice 15 e vai até o final
print(f'Range [15:]: {frase[15:]}')

#Slice começa no índice 9 e vai até o final pulando de 3 em 3
print(f'Range[9::3]: {frase[9::3]}')

# Comprimento de frase
print(f'Comprimento da String: {len(frase)} caracteres.')

# Conta quantas ocorrências de um determinado caractere aparecem 
print(f'Contagem de caracteres "o": {frase.count('o')}')

# Conta quantas vezes a letra o aparece até a posição 13
print(f'Contagem de "o" até 13: {frase.count('o', 0, 13)}') 

# Retorna a posição onde a sequência de caracteres começa
print(frase.find('deo'))

# Uma string inexistente retorna -1
print(frase.find('Android'))

# Verifica se a string Curso existe em frase
print(f'Verifica se a string Curso existe em frase: {"Curso" in frase}')

# Substitui uma string por outra
print(frase.replace('Python','Android')) 

# Escrever a frase em caixa alta
print(frase.upper()) 

# Escreve a frase em caixa baixa
print(frase.lower()) 

# Escreve a primeira letra da primeira palavra em maiúscula e as demais em minúsculas.
print(frase.capitalize())

# Escreve cada primeira letra de cada palavra em maiúscula
print(frase.title())

# Imprime a frase2
print(frase2)

# Remove espaços antes e depois da string
print(frase2.strip())

# Tira os espaços em branco à direita
print(frase2.rstrip())

# Remove os espaços à esquerda da string
print(frase2.lstrip())


# -------------- Divisão ------------------
# Quebra a string onde tem espaços
# Gera uma lista com todas as palavras de uma cadeia de caracteres
print(frase.split())

# Divide a cadeia de caracteres
lista = frase.split()

# Acessa a primeira palavra da lista dividida
print(lista[0])

# Retorna o caractere que ocupa o índice 2 da primeira palavra(0).
print(lista[0][2])

# Juntar os elementos usando o separador informado
print('-'.join(lista))

# -------Texto longo ------------------
# Use 3 aspas para imprimir um texto longo que quebra linhas
print("""
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""")

# Combinando funções
print(frase.upper().count('O'))


