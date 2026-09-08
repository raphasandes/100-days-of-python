# Aula 12 — Percorrendo listas de dicionários com `for`

## Objetivo da aula

Nesta aula, aprofundamos o trabalho com listas de dicionários e aprendemos a percorrer seus elementos diretamente utilizando o `for`.

O principal objetivo foi compreender a diferença entre:

- percorrer uma lista utilizando índices;
- percorrer diretamente os elementos de uma lista;
- acessar valores de um dicionário durante cada volta do `for`;
- realizar cálculos e condições com os dados de cada dicionário.

---

## 1. Estrutura utilizada

Trabalhamos com uma lista contendo vários dicionários:

```python
produtos = [
    {
        "nome": "SmartPOS",
        "vendas": 180,
        "meta": 200
    },
    {
        "nome": "Tap to Phone",
        "vendas": 250,
        "meta": 220
    },
    {
        "nome": "Link de Pagamento",
        "vendas": 140,
        "meta": 150
    }
]
```

Cada elemento da lista `produtos` é um dicionário.

Assim:

```python
produtos[0]
```

retorna o primeiro dicionário inteiro.

Também podemos acessar uma informação específica:

```python
produtos[0]["vendas"]
```

Resultado:

```text
180
```

---

## 2. Percorrendo uma lista com índices

Uma forma já estudada anteriormente é:

```python
for indice in range(len(produtos)):
    print(produtos[indice])
```

Nesse caso:

- `len(produtos)` identifica a quantidade de elementos;
- `range()` gera os números dos índices;
- `indice` recebe `0`, depois `1`, depois `2`;
- `produtos[indice]` acessa cada elemento da lista.

O caminho pode ser entendido como:

```text
índice → lista → elemento
```

---

## 3. Percorrendo diretamente os elementos

Também podemos utilizar:

```python
for produto in produtos:
    print(produto)
```

Nesse caso, não precisamos trabalhar com os índices.

A cada volta do `for`, a variável `produto` recebe diretamente um elemento da lista.

Como cada elemento da lista é um dicionário:

```text
1ª volta → produto recebe o primeiro dicionário
2ª volta → produto recebe o segundo dicionário
3ª volta → produto recebe o terceiro dicionário
```

Portanto, o `for` consegue percorrer diretamente todos os elementos da lista.

---

## 4. Acessando informações durante o `for`

Como `produto` representa um dicionário inteiro em cada volta, podemos acessar suas chaves:

```python
for produto in produtos:
    print(produto["nome"])
```

Saída:

```text
SmartPOS
Tap to Phone
Link de Pagamento
```

Também podemos acessar mais de uma informação:

```python
for produto in produtos:
    print("Produto:", produto["nome"])
    print("Vendas:", produto["vendas"])
```

Os dois comandos pertencem ao bloco do `for`.

Por isso, são executados para o mesmo produto antes de o `for` passar para o próximo elemento.

---

## 5. `for` com condições

Podemos combinar o `for` com o `if`:

```python
for produto in produtos:
    if produto["vendas"] >= produto["meta"]:
        print(produto["nome"], "atingiu a meta")
```

A cada volta:

1. `produto` recebe um dicionário;
2. o Python acessa `vendas`;
3. o Python acessa `meta`;
4. o `if` compara os dois valores;
5. o `print()` só é executado se a condição for verdadeira.

No exemplo:

```text
SmartPOS → 180 >= 200 → False
Tap to Phone → 250 >= 220 → True
Link de Pagamento → 140 >= 150 → False
```

Saída:

```text
Tap to Phone atingiu a meta
```

---

## 6. Criando uma variável durante o `for`

Também podemos realizar cálculos utilizando os valores dos dicionários:

```python
for produto in produtos:
    diferenca = produto["vendas"] - produto["meta"]
    print(produto["nome"], diferenca)
```

Resultado:

```text
SmartPOS -20
Tap to Phone 30
Link de Pagamento -10
```

A variável `diferenca` recebe um novo valor em cada volta do `for`.

Isso acontece porque `produto` também representa um dicionário diferente em cada volta.

---

## 7. Interpretando os resultados

O resultado da diferença entre vendas e meta também pode ser interpretado:

```python
for produto in produtos:
    diferenca = produto["vendas"] - produto["meta"]

    if diferenca >= 0:
        print(produto["nome"], "acima da meta")
    else:
        print(produto["nome"], "abaixo da meta")
```

Saída:

```text
SmartPOS abaixo da meta
Tap to Phone acima da meta
Link de Pagamento abaixo da meta
```

Nesse código:

### `for produto in produtos:`

Percorre os elementos da lista.

A cada volta, `produto` recebe um dos dicionários.

### `diferenca = produto["vendas"] - produto["meta"]`

Calcula a diferença entre vendas e meta e armazena o resultado na variável `diferenca`.

### `if diferenca >= 0:`

Testa uma condição.

Se a diferença for maior ou igual a zero, o produto atingiu ou superou sua meta.

Caso contrário, o bloco do `else` é executado.

---

## Principal aprendizado da aula

Existem diferentes formas de percorrer uma lista.

Podemos percorrer seus índices:

```python
for indice in range(len(produtos)):
    print(produtos[indice])
```

Ou podemos percorrer diretamente seus elementos:

```python
for produto in produtos:
    print(produto)
```

Quando percorremos diretamente uma lista de dicionários, a variável do `for` recebe um dicionário inteiro em cada volta.

Assim, podemos acessar suas informações:

```python
produto["nome"]
produto["vendas"]
produto["meta"]
```

e utilizá-las para realizar cálculos, comparações e análises.

---

## Próxima aula

Retomar a partir da combinação de:

- listas de dicionários;
- `for`;
- acesso às chaves;
- variáveis calculadas;
- `if` e `else`.

Antes de avançar para novos conteúdos, reforçar a interpretação do fluxo completo de um pequeno programa de análise de dados.