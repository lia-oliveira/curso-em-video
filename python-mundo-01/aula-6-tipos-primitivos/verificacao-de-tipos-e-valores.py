# ================================
#         Teoria
# ================================

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
print(f'A soma entre {n1} e {n2} é {soma}.')



# tipos booleanos só serão falsos quando o valores forem:
# false
# none
# Zero de qualquer tipo numérico
# Coleções vazias
# Objetos que implementam __bool__() ou __len__() retornando false ou 0
n = bool(input('Digite um valor: '))
print(type(n))
print(n)

# isnumeric() verifica se é possível converter uma string em valor numérico
sobrenome='da Silva'
telefone= '2199999999'
print(sobrenome.isnumeric()) # False
print(telefone.isnumeric()) # True

# isalpha() verifica se são letras
# Não pode haver espaços para que retorne True
cor='azul'
cor2='cor de rosa'
cor3= 'verde3'
cor4= '4'
cor5= 5
print(cor.isalpha())  # True
print(cor2.isalpha()) # False

# isalnum() identifica letras e números
# Retorna true quando a string tem:
# apenas letras
# apenas números (entre aspas)
# letras e números
print(cor.isalnum()) # True
print(cor2.isalnum()) # False
print(cor3.isalnum()) # True
print(cor4.isalnum()) # True
#print(cor5.isalnum()) #AttributeError: 'int' object has no attribute 'isalnum'


