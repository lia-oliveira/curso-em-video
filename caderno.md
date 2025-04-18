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


## Manipulando Cadeias de Caracteres


# Banco de Dados MySQL

## Aula 03: Criando o primeiro banco de dados

Banco de dados contém tabelas.
Tabelas contém registros.
Registros são compostos por campos.

Tabela pessoas:
* nome
* idade
* sexo
* peso
* altura
* nacionalidade

### Tipos Primitivos

1.Numérico
* Inteiro: TinyInt, SmallInt, Int, MediumInt, BigInt
* Real: Decimal, Float, Double, Real
* Lógico: Bit, Boolean

2.Data/Tempo: Date, DateTime, TimeStamp, Time, Year

3.Literal
* Caractere: char, varchar
* Texto: TinyText, Text, MediumText, LongText
* Binário: TinyBlob, Blob, MediumBlob, LongBlob
* Coleção: enum, set

4.Espacial: Geometry, point, polygon, multiPlygon

### Comandos de terminal
Você precisa estar com o servidor ativo.
Abra o terminal do MySQL e quando ele pedir a senha, pressione Enter.

#### Mostra todas as bases de dados criadas
```
show databases
```

#### Abre o banco de dados desejado (use nomeDoBanco)
```
use cadastro
```

#### Saber qual banco de dados está aberto
```
status
```

#### Mostra as tabelas existentes
```
show tables
```

#### Descreve a tabela escolhida
```
describe pessoas
```

#### Sair do terminal
```
exit
```

# Padrão de codificação de caracteres (UTF-8)

Para evitar que os acentos fiquem desconfigurados podemos configurar o padrão de caracteres a ser utilizado já na criação do banco de dados. O `utf8` está depreciado. Vamos utilizar `utf8mb4`.

Forma 1:

```sql
CREATE DATABASE cadastro
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;
```

Forma 2:

```sql
CREATE DATABASE IF NOT EXISTS cadastro
DEFAULT CHARSET = utf8mb4
DEFAULT COLLATE = utf8mb4_general_ci;
```

Forma 3 (via terminal)
```sql
CREATE DATABASE nome_do_banco CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

# Criação de tabelas

