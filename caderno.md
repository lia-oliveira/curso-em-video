# Caderno


# Importação de bibliotecas e módulos

Anotações baseadas no conteúdo da aula 008.

## Importação da Biblioteca Inteira

Sintaxe: `import nomeDaBiblioteca`

```txt
import math
```

Para utilizar um método é necesário colocar o nome da biblioteca seguido de ponto antes de escrever o nome da função.

```py
raiz = math.sqrt(num)
```

## Importação de um módulo ou mais

Sintaxe: from biblioteca import modulo

```py
from math import sqrt
```
Quando a importação é feita referenciando o nome do módulo, não é necessário fazer a chamada utilizando o nome da bilbioteca.

```py
raiz = sqrt(num)
```

Importação de mais de um módulo na mesma linha:

```py
from math import sqrt, floor, ceil
```


## Funcionalidades da biblioteca math

Biblioteca math:
* ceil -> arredondamento
* floot -> arredondamento para baixo
* trunc -> truca o número eliminando o que estiver após a vírgula
* pow -> potência
* sqrt -> Raiz quadrada
* factorial ->  cálculo de fatorial


Exemplo de aplicação:

```py
from math import sqrt, floor, ceil

num = int(input('Digite um númeo: '))
raiz = sqrt(num)

print(' A raiz de {} é igual a {}'.format(num, floor(raiz)))
print(' A raiz de {} é igual a {}'.format(num, ceil(raiz)))
```

# Geração de números pseudoaleatórios

O número gerado a partir do método random() vai vestar no range entre 0 e 1.
```py
import random
num2 = random.random()
print(num2)
```
## Números pseudoaleatórios inteiros
Ao usar o randint(num_menor, num_maior) você deve informar o range onde o número deve estar. Caso não informe nenhum número ou apenas 1, vai recerber um TypeError.

```py
import random
num3 = random.randint(1,10)
print(num3)
```


# Manipulando Cadeias de Caracteres

