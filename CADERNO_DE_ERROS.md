# Dia 07 — Funções

## Erro 1 — Sintaxe incorreta no `print()`

### Tentativa

```python
print(f{"Meu nome é Raphael." </> "Estou aprendendo Python.")
```

### Problema

Foram misturados elementos de `f-string`, chaves e símbolos que não fazem parte da sintaxe válida do Python.

### Correção

```python
print("Meu nome é Raphael.")
print("Estou aprendendo Python.")
```

### Aprendizado

Para imprimir duas mensagens em linhas diferentes, posso utilizar dois comandos `print()`.

---

## Erro 2 — Parêntese não fechado

### Tentativa

```python
print("RELATÓRIO"
```

### Problema

O parêntese do comando `print()` não foi fechado.

### Correção

```python
print("RELATÓRIO")
```

### Aprendizado

Parênteses e aspas precisam ser abertos e fechados corretamente. Caso contrário, o programa apresenta um erro de sintaxe.

---

## Erro 3 — Símbolo que não existe em Python

### Tentativa

```text
</>
```

### Problema

O símbolo foi utilizado para representar uma linha vazia, mas não é um comando válido em Python.

### Correção

```python
print()
```

### Aprendizado

Um `print()` sem conteúdo produz uma linha em branco.

---

## Erro 4 — Função chamada antes de ser definida

### Tentativa

```python
cumprimentar()


def cumprimentar():
    print("Olá!")
```

### Problema

O Python tentou executar `cumprimentar()` antes de encontrar sua definição.

### Correção

```python
def cumprimentar():
    print("Olá!")


cumprimentar()
```

### Aprendizado

O Python executa o programa de cima para baixo. Por isso, uma função precisa ser definida antes de ser chamada.

---

## Erro 5 — Parâmetro declarado, mas não utilizado

### Tentativa

```python
def titulo1(texto):
    print("RELATÓRIO DE VENDAS")
```

### Problema

A função recebeu o parâmetro `texto`, mas não o utilizou. Em vez disso, imprimiu sempre uma mensagem fixa.

### Correção

```python
def titulo(texto):
    print(texto)
```

### Aprendizado

Um parâmetro permite enviar informações diferentes para a mesma função. Para cumprir esse objetivo, ele precisa ser utilizado dentro dela.

---

## Erro 6 — Função chamada sem o argumento necessário

### Tentativa

```python
def titulo(texto):
    print(texto)


titulo()
```

### Problema

A função esperava receber um valor para o parâmetro `texto`, mas foi chamada sem nenhuma informação.

### Correção

```python
titulo("RELATÓRIO DE VENDAS")
```

### Aprendizado

Quando uma função possui um parâmetro obrigatório, é necessário fornecer um argumento ao chamá-la.

---

## Correção conceitual — Uso de memória

Inicialmente, considerei que utilizar funções necessariamente faria o programa consumir menos memória.

A principal vantagem das funções, porém, está na organização, reutilização e manutenção do código.

Em alguns casos, uma chamada de função pode até gerar um pequeno custo adicional de execução. Mesmo assim, esse custo costuma ser irrelevante diante dos benefícios de um código mais claro e fácil de modificar.


---

# Dia 09 — Consolidação de Funções, Listas e Índices

## Erro 1 — Confundir o índice com o valor da lista

### Tentativa

Ao analisar a próxima repetição do `for`, considerei que:

```text
numero = Carlos
```

### Problema

A variável `numero` não recebe diretamente os elementos da lista.

No código:

```python
for numero in range(len(funcionarios)):
```

`numero` recebe os valores produzidos por `range()`:

```text
0, 1, 2
```

Esses números são utilizados como índices para acessar os elementos da lista.

### Correção

Na segunda repetição:

```text
numero = 1
funcionarios[1] = "Carlos"
```

### Aprendizado

O índice e o valor encontrado são coisas diferentes.

```text
numero = 1 → índice
funcionarios[1] = "Carlos" → valor
```

Regra para lembrar:

> O índice diz ONDE procurar.  
> A lista retorna O QUE está naquela posição.

---

## Erro 2 — Escrever incorretamente `len()`

### Tentativas

Durante os exercícios, apareceram:

```python
leng(produtos)
```

e:

```python
leg(projetos)
```

### Problema

Essas funções não existem.

A função utilizada para descobrir a quantidade de elementos de uma lista é:

```python
len()
```

### Correção

```python
len(produtos)
```

ou:

```python
len(projetos)
```

### Aprendizado

Uma associação útil é:

```text
len → length → tamanho/comprimento
```

`len()` informa quantos elementos existem na lista.

---

## Erro 3 — Esquecer aspas em valores de texto

### Tentativa

```python
produtos = [SmartPOS, Tap to Phone, Link de Pagamento, Pix no POS]
```

### Problema

Os nomes dos produtos são textos.

Sem aspas, o Python não interpreta esses elementos como strings.

### Correção

```python
produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento", "Pix no POS"]
```

### Aprendizado

Valores de texto devem ser representados como strings.

```python
"SmartPOS"
```

é um texto.

---

## Erro 4 — Esquecer os dois pontos na definição da função

### Tentativa

```python
def consolidacao(produto, cliente)
```

### Problema

A definição de uma função precisa terminar com dois pontos (`:`).

### Correção

```python
def consolidacao(produto, cliente):
```

### Aprendizado

Ao criar uma função com `def`, devo lembrar da estrutura:

```text
def + nome + (parâmetros) + :
```

Exemplo:

```python
def mostrar_produto(produto, preco):
```

---

## Erro 5 — Utilizar um nome de variável diferente do que foi criado

### Tentativa

A lista foi criada como:

```python
quantidade = [185, 92, 143, 76]
```

mas posteriormente foi utilizada:

```python
consolidacao(produtos[indice], clientes[indice])
```

### Problema

Não havia nenhuma variável chamada `clientes` definida no programa.

O nome utilizado para acessar a lista precisa corresponder ao nome da variável que foi criada.

### Correção

```python
consolidacao(produtos[indice], quantidade[indice])
```

### Aprendizado

É necessário manter consistência nos nomes das variáveis.

Se a lista foi criada como:

```python
quantidade = [...]
```

devo utilizar:

```python
quantidade[indice]
```

para acessar seus elementos.

---

## Correção conceitual — `for`, lista, índice e parâmetro

Durante a aula também foi necessário ajustar o vocabulário utilizado para explicar o código.

No exemplo:

```python
produtos = ["SmartPOS", "Tap to Phone"]

def mostrar_produto(produto):
    print(produto)

for indice in range(len(produtos)):
    mostrar_produto(produtos[indice])
```

Temos:

```text
produtos        → lista
produto         → parâmetro
indice          → variável do for utilizada como índice
for             → estrutura de repetição
mostrar_produto → função
```

### Aprendizado

Usar o vocabulário correto ajuda a compreender o papel de cada elemento do programa.

Principalmente:

> `for` não é uma função: é uma estrutura de repetição.

> `produtos` não é uma função: é uma lista.

> `produto` é um parâmetro da função.

> `indice` recebe os números produzidos pelo `range()` e pode ser utilizado para acessar posições das listas.