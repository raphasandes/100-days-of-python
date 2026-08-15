# Aprendizados — Dia 09

## Objetivo

A Aula 09 foi uma aula de consolidação.

O principal objetivo foi reforçar a combinação entre:

- funções;
- parâmetros;
- argumentos;
- listas;
- índices;
- `for`;
- `range()`;
- `len()`.

O conteúdo já havia sido trabalhado anteriormente, mas ainda precisava ser praticado antes de avançar para novos conceitos.

---

## 1. Lista x parâmetro

Uma lista armazena vários valores:

```python
funcionarios = ["Ana", "Carlos", "Marina"]
```

Um parâmetro é uma variável definida dentro da estrutura de uma função para receber um valor quando ela for chamada:

```python
def mostrar_funcionario(funcionario):
    print(funcionario)
```

Nesse exemplo:

- `funcionarios` = lista;
- `funcionario` = parâmetro.

Uma forma de lembrar:

```text
funcionarios → guarda vários nomes
funcionario → recebe um nome em uma execução da função
```

---

## 2. Índice x valor

O índice representa a posição de um elemento dentro de uma lista.

```python
funcionarios = ["Ana", "Carlos", "Marina"]
```

Temos:

```text
índice 0 → Ana
índice 1 → Carlos
índice 2 → Marina
```

Portanto:

```python
funcionarios[2]
```

resulta em:

```text
Marina
```

Uma forma importante de lembrar:

```text
índice → diz ONDE procurar
valor → é O QUE encontramos naquela posição
```

---

## 3. len() x range()

Essa diferença foi especialmente reforçada durante a aula.

`len()` informa a quantidade de elementos:

```python
clientes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

len(clientes)
```

Resultado:

```text
5
```

Já:

```python
range(len(clientes))
```

permite percorrer:

```text
0, 1, 2, 3, 4
```

Portanto:

```text
len() → QUANTOS elementos existem

range() → sequência de números que será percorrida
```

---

## 4. Variável do for

No código:

```python
for indice in range(len(produtos)):
```

`indice` é a variável do `for`.

Ela recebe, a cada repetição, um dos números produzidos pelo `range()`.

Exemplo:

```text
1ª repetição → indice = 0
2ª repetição → indice = 1
3ª repetição → indice = 2
```

Esses valores podem ser usados como índices:

```python
produtos[indice]
```

---

## 5. Duas listas relacionadas

Quando duas listas possuem elementos correspondentes nas mesmas posições, podemos utilizar o mesmo índice.

```python
produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento"]
precos = [150, 100, 80]
```

Relação:

```text
índice 0 → SmartPOS       → 150
índice 1 → Tap to Phone   → 100
índice 2 → Link de Pagamento → 80
```

Assim:

```python
produtos[indice]
precos[indice]
```

acessam informações correspondentes.

---

## 6. Do índice até o parâmetro

Um dos principais aprendizados da aula foi compreender todo o caminho realizado pelo programa.

Exemplo:

```python
for indice in range(len(funcionarios)):
    mostrar_funcionario(funcionarios[indice], salarios[indice])
```

Se:

```text
indice = 2
```

então:

```text
funcionarios[2] → João
salarios[2] → 3800
```

A chamada passa a ser:

```python
mostrar_funcionario("João", 3800)
```

E os parâmetros recebem:

```text
funcionario → João
salario → 3800
```

Portanto, o caminho pode ser resumido como:

```text
índice
↓
posição da lista
↓
valor encontrado
↓
argumento
↓
parâmetro
↓
execução da função
```

---

## 7. Erros encontrados durante a prática

### Esquecer `def`

Foi escrito inicialmente:

```python
mostrar_produto(produto, preco):
```

O correto é:

```python
def mostrar_produto(produto, preco):
```

### Confundir o nome de len()

Durante os exercícios apareceram:

```python
leng(produtos)
```

e:

```python
leg(projetos)
```

O correto é:

```python
len(produtos)
```

Uma associação útil é:

```text
len → length → tamanho/comprimento
```

### Esquecer os dois pontos

Foi escrito:

```python
def consolidacao(produto, cliente)
```

O correto é:

```python
def consolidacao(produto, cliente):
```

### Esquecer aspas em textos

Foi escrito:

```python
produtos = [SmartPOS, Tap to Phone]
```

Para representar textos, é necessário:

```python
produtos = ["SmartPOS", "Tap to Phone"]
```

### Utilizar um nome de variável que não existe

A lista havia sido criada como:

```python
quantidade = [185, 92, 143, 76]
```

mas posteriormente foi utilizada uma variável chamada:

```python
clientes[indice]
```

Como `clientes` não havia sido criada, o nome correto era:

```python
quantidade[indice]
```

---

## 8. Vocabulário reforçado

É importante utilizar corretamente os termos:

- `for` → estrutura de repetição;
- `produtos` → lista;
- `indice` → variável do `for` utilizada como índice;
- `produto` → parâmetro da função;
- `"SmartPOS"` → valor que pode ser passado como argumento;
- `len()` → função que informa a quantidade de elementos;
- `range()` → função que produz uma sequência de números.

---

## Evolução

No início do reforço, ainda havia dificuldade principalmente em conectar:

```text
for + índice + lista + função + parâmetro
```

Ao final da Aula 09, foi possível construir de forma autônoma um programa utilizando:

```python
produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento", "Pix no POS"]
quantidade = [185, 92, 143, 76]


def consolidacao(produto, cliente):
    print("Produto:", produto)
    print("Clientes ativos:", cliente)


for indice in range(len(produtos)):
    consolidacao(produtos[indice], quantidade[indice])
```

A lógica central está mais consolidada.

Os erros que ainda apareceram estiveram principalmente relacionados à sintaxe, à memorização de `len()` e ao uso correto dos nomes das variáveis.

Na próxima aula, podemos avançar para novos conteúdos, mantendo revisões curtas dos conceitos anteriores para fortalecer a aprendizagem.