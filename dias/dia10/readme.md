# Dia 10 — Consolidação e Revisão para a Prova 2

## Objetivo da aula

A Aula 10 foi dedicada à consolidação dos conteúdos estudados até aqui e à preparação para a Prova 2.

Não foram introduzidos novos conceitos.

O foco principal foi aumentar a dificuldade dos exercícios e verificar se os conceitos já estudados poderiam ser utilizados de forma mais autônoma.

---

## Conteúdos revisados

- Variáveis
- Tipos básicos (`str`, `int` e números)
- `print()`
- Listas
- Índices
- `len()`
- `range()`
- `for`
- Funções com `def`
- Parâmetros
- Argumentos
- Chamadas de função
- f-strings
- Integração entre funções, listas, índices e estruturas de repetição

---

## Listas e parâmetros

Durante as aulas anteriores, uma das principais dificuldades foi compreender a diferença entre uma lista e o parâmetro de uma função.

Exemplo:

```python
produtos = ["SmartPOS", "Tap to Phone", "Pix no POS"]

def mostrar_produto(produto):
    print("Produto:", produto)
```

Neste caso:

- `produtos` é uma lista que armazena vários valores.
- `produto` é um parâmetro da função.
- O parâmetro recebe um valor quando a função é chamada.

---

## `len()`, `range()` e índices

Exemplo:

```python
produtos = ["SmartPOS", "Tap to Phone", "Pix no POS"]
```

O comando:

```python
len(produtos)
```

retorna:

```text
3
```

Isso significa que a lista possui três elementos.

Já:

```python
range(len(produtos))
```

permite trabalhar com:

```text
0, 1, 2
```

Esses valores podem ser utilizados como índices da lista.

Exemplo:

```python
for numero in range(len(produtos)):
    print(produtos[numero])
```

O `for` faz a variável `numero` assumir, a cada volta, um dos valores produzidos pelo `range()`.

---

## Trabalhando com listas paralelas

Exemplo:

```python
produtos = ["SmartPOS", "Tap to Phone", "Pix no POS"]
vendas = [185, 92, 76]
```

Podemos utilizar o mesmo índice para acessar informações correspondentes:

```python
for numero in range(len(produtos)):
    print(produtos[numero], vendas[numero])
```

Na primeira volta:

```text
numero = 0
produtos[0] = SmartPOS
vendas[0] = 185
```

Na segunda:

```text
numero = 1
produtos[1] = Tap to Phone
vendas[1] = 92
```

Na terceira:

```text
numero = 2
produtos[2] = Pix no POS
vendas[2] = 76
```

---

## Integração com funções

Também consolidamos a utilização desses valores como argumentos de uma função:

```python
def analisar(produto, quantidade):
    print(produto, quantidade)

for numero in range(len(produtos)):
    analisar(produtos[numero], vendas[numero])
```

O fluxo pode ser compreendido como:

```text
lista
↓
len()
↓
range()
↓
for
↓
índice
↓
valor armazenado na lista
↓
argumento enviado para a função
↓
parâmetro recebe o valor
↓
execução da função
```

---

## f-strings

Revisamos também as f-strings.

Exemplo:

```python
produto = "SmartPOS"
quantidade = 185

mensagem = f"{produto}: {quantidade} vendas"

print(mensagem)
```

A letra `f` permite inserir valores ou expressões dentro de uma string utilizando `{}`.

---

## Principais erros observados

Durante os exercícios, apareceram principalmente erros de sintaxe.

### Parêntese não fechado

Incorreto:

```python
print("RELATÓRIO DE PRODUTOS"
```

Correto:

```python
print("RELATÓRIO DE PRODUTOS")
```

### Ausência de `:` na função

Incorreto:

```python
def relatorio_produtos(produto, cliente, faturamento)
```

Correto:

```python
def relatorio_produtos(produto, cliente, faturamento):
```

### Confusão entre lista e parâmetro

Lista:

```python
quantidades
```

Parâmetro:

```python
quantidade
```

Dentro da função, utilizamos o parâmetro.

Na chamada da função, podemos acessar um elemento da lista:

```python
mostrar_produto(produtos[numero], quantidades[numero])
```

---

## Diagnóstico ao final da aula

Os conceitos de variáveis, listas, índices, `len()` e `for` estão consolidados.

A compreensão de funções e parâmetros apresentou evolução significativa.

A integração entre `range()`, índices, listas e funções já é compreendida, mas ainda precisa de prática para se tornar automática.

Esse será um dos pontos observados na Prova 2.

---

## Direção do aprendizado

O objetivo principal do estudo de Python é sua aplicação em análise e ciência de dados.

Por isso, o aprendizado da linguagem será direcionado aos fundamentos necessários para trabalhar futuramente com:

- manipulação de dados;
- limpeza e transformação de bases;
- análise exploratória;
- visualização de dados;
- estatística aplicada;
- automação de análises;
- bibliotecas como `pandas`;
- preparação de dados;
- fundamentos de ciência de dados e modelagem.

O objetivo não é estudar toda a linguagem Python antes de começar a trabalhar com dados, mas construir progressivamente a base necessária para utilizá-la de forma consciente.

---

## Próxima aula

A próxima aula será dedicada à:

# Prova 2

A prova encerrará o segundo ciclo de cinco aulas e servirá para avaliar o nível de consolidação dos conteúdos estudados até aqui.