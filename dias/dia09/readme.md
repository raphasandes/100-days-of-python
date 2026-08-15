# Dia 09 — Consolidação: Funções, Listas e Índices

## Objetivo da aula

Esta aula foi dedicada à consolidação dos conteúdos trabalhados anteriormente, especialmente a combinação entre funções, listas, índices e estruturas de repetição.

O objetivo principal foi compreender melhor como diferentes partes de um programa se relacionam:

- listas;
- índices;
- `for`;
- `range()`;
- `len()`;
- funções;
- parâmetros;
- argumentos.

Não foram introduzidos novos conteúdos. O foco foi reforçar a lógica e construir programas completos com maior autonomia.

---

## 1. Listas e parâmetros

Uma das principais distinções trabalhadas foi a diferença entre uma lista e um parâmetro.

Exemplo:

```python
funcionarios = ["Ana", "Carlos", "Marina"]

def mostrar_funcionario(funcionario):
    print("Funcionário:", funcionario)
```

Nesse exemplo:

- `funcionarios` é uma lista que armazena vários valores;
- `funcionario` é um parâmetro da função;
- o parâmetro recebe temporariamente um valor enviado para a função.

---

## 2. Índices

Os índices representam as posições dos elementos dentro de uma lista.

Exemplo:

```python
funcionarios = ["Ana", "Carlos", "Marina"]
```

As posições são:

```text
funcionarios[0] → Ana
funcionarios[1] → Carlos
funcionarios[2] → Marina
```

Uma lista com três elementos possui índices de `0` até `2`.

---

## 3. len()

A função `len()` informa a quantidade de elementos existentes em uma lista.

Exemplo:

```python
funcionarios = ["Ana", "Carlos", "Marina"]

print(len(funcionarios))
```

Resultado:

```text
3
```

Portanto:

```text
len() → quantidade de elementos
```

---

## 4. range()

`range()` produz uma sequência de números que pode ser utilizada em uma estrutura de repetição.

Exemplo:

```python
range(3)
```

Ao ser percorrido por um `for`, produz:

```text
0
1
2
```

Assim:

```text
len(funcionarios) → 3

range(len(funcionarios)) → 0, 1, 2
```

---

## 5. for e índices

Podemos utilizar os números produzidos por `range()` como índices de uma lista.

```python
funcionarios = ["Ana", "Carlos", "Marina"]

for indice in range(len(funcionarios)):
    print(funcionarios[indice])
```

Durante as repetições:

```text
indice = 0 → funcionarios[0] → Ana
indice = 1 → funcionarios[1] → Carlos
indice = 2 → funcionarios[2] → Marina
```

O `indice` indica onde procurar um elemento na lista.

---

## 6. Trabalhando com duas listas relacionadas

Também trabalhamos com listas cujos elementos possuem correspondência pela posição.

```python
funcionarios = ["Ana", "Carlos", "Marina"]
salarios = [3500, 4200, 5100]
```

As relações são:

```text
posição 0 → Ana    → 3500
posição 1 → Carlos → 4200
posição 2 → Marina → 5100
```

Podemos utilizar o mesmo índice para acessar as duas listas:

```python
for indice in range(len(funcionarios)):
    print(funcionarios[indice])
    print(salarios[indice])
```

---

## 7. Funções combinadas com listas

O principal exercício da aula foi combinar todos esses conceitos.

```python
funcionarios = ["Marcos", "Fernanda", "João", "Beatriz"]
salarios = [3200, 4500, 3800, 5100]

def mostrar_funcionario(funcionario, salario):
    print("Funcionário:", funcionario)
    print("Salário:", salario)

for indice in range(len(funcionarios)):
    mostrar_funcionario(funcionarios[indice], salarios[indice])
```

O caminho realizado pelo programa pode ser entendido como:

```text
lista
↓
índice
↓
elemento da lista
↓
argumento enviado para a função
↓
parâmetro
↓
execução da função
```

---

## 8. Conceitos importantes consolidados

### Lista

Armazena vários valores.

```python
produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento"]
```

### Índice

Representa a posição de um elemento.

```python
produtos[0]
```

### Parâmetro

Variável definida na função que recebe um valor quando a função é chamada.

```python
def mostrar_produto(produto):
```

`produto` é o parâmetro.

### Argumento

É o valor enviado para a função.

```python
mostrar_produto("SmartPOS")
```

`"SmartPOS"` é o argumento.

### len()

Informa quantos elementos existem.

### range()

Produz uma sequência de números.

### for

Executa uma repetição para cada valor da sequência percorrida.

---

## 9. Uma forma de visualizar

Uma das principais conclusões da aula foi:

```text
indice → diz ONDE procurar
parâmetro → recebe O QUE foi encontrado
```

Exemplo:

```text
indice = 2

funcionarios[2] → João

mostrar_funcionario("João", 3800)

funcionario → João
salario → 3800
```

---

## Evolução

### Pontos reforçados nesta aula

- Diferença entre lista e parâmetro.
- Diferença entre índice e valor.
- Funcionamento de `len()`.
- Funcionamento de `range()`.
- Uso de índices dentro do `for`.
- Correspondência entre elementos de duas listas.
- Passagem de valores para funções.
- Relação entre argumentos e parâmetros.
- Construção de funções combinadas com estruturas de repetição.

### Resultado

Ao final da aula, foi possível construir de forma autônoma um programa combinando:

```text
listas + len() + range() + for + índices + funções + parâmetros
```

O conteúdo trabalhado nas aulas anteriores apresentou evolução significativa e está mais consolidado.

Na próxima aula, será possível avançar para novos conteúdos, mantendo pequenas revisões desses conceitos ao longo dos exercícios.