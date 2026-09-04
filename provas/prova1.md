# Prova 01 — Fundamentos de Python

**Data:** 23/07/2026
**Nota:** 9,25 / 10
**Questões:** 6
**Resultado:** Aprovado

---

# Objetivo da prova

A Prova 01 teve como objetivo avaliar os fundamentos estudados no primeiro ciclo do curso de Python.

Os principais conteúdos avaliados foram:

* variáveis;
* tipos de dados;
* `str`;
* `int`;
* `float`;
* `bool`;
* `print()`;
* `input()`;
* comparações;
* estruturas condicionais;
* `if`;
* `elif`;
* `else`;
* listas;
* índices;
* `len()`;
* `for`;
* `range()`;
* leitura e interpretação de código.

---

# Questão 1 — Fundamentos

**Pontuação:** 1,0 / 1,0

A primeira questão avaliou os conceitos básicos da linguagem Python, incluindo variáveis, armazenamento de valores e tipos de dados.

## Conteúdos avaliados

```python
nome = "Raphael"
idade = 34
altura = 1.75
```

Os exemplos representam diferentes tipos de dados:

```text
"Raphael" → str
34        → int
1.75      → float
```

Também foi avaliada a compreensão de que uma variável pode armazenar um valor para que ele seja utilizado posteriormente pelo programa.

### Avaliação

Conceitos fundamentais compreendidos.

---

# Questão 2 — Entrada e saída de dados

**Pontuação:** 1,0 / 1,0

A questão avaliou a compreensão dos comandos:

```python
print()
```

e:

```python
input()
```

## Aprendizado

`print()` é utilizado para mostrar informações na tela.

Exemplo:

```python
print("Olá, Raphael!")
```

`input()` permite receber uma informação digitada pelo usuário.

Exemplo:

```python
nome = input("Digite seu nome: ")
```

O valor recebido pode ser armazenado em uma variável e utilizado posteriormente.

### Avaliação

Compreensão adequada da diferença entre entrada e saída de dados.

---

# Questão 3 — Condições

**Pontuação:** 1,0 / 1,0

A questão avaliou a utilização de:

```python
if
elif
else
```

Essas estruturas permitem que o programa tome decisões dependendo de determinadas condições.

Exemplo:

```python
idade = 18

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

## Aprendizado

O `if` verifica uma condição.

O `elif` permite verificar outra condição quando a anterior não foi atendida.

O `else` determina o que deve acontecer quando as condições anteriores não forem atendidas.

### Avaliação

Estruturas condicionais compreendidas.

---

# Questão 4 — Listas e índices

**Pontuação:** 0,75 / 1,0

A questão avaliou a compreensão de listas e o acesso aos seus elementos por meio de índices.

Exemplo:

```python
nomes = ["Raphael", "Lucas", "Ana"]
```

Os índices são:

```text
"Raphael" → índice 0
"Lucas"   → índice 1
"Ana"     → índice 2
```

Assim:

```python
print(nomes[0])
```

retorna:

```text
Raphael
```

E:

```python
print(nomes[2])
```

retorna:

```text
Ana
```

## Aprendizado

Python começa a contar os índices a partir de:

```text
0
```

Portanto, uma lista com três elementos possui os índices:

```text
0, 1, 2
```

### Avaliação

Boa compreensão de listas e índices, com pequenos pontos ainda a consolidar.

---

# Questão 5 — `len()`, `range()` e `for`

**Pontuação:** 2,0 / 2,0

Esta foi uma das partes mais importantes da prova.

Foram avaliados:

```python
len()
range()
for
```

## `len()`

Considere:

```python
nomes = ["Raphael", "Lucas", "Ana"]
```

O comando:

```python
len(nomes)
```

retorna:

```text
3
```

porque existem três elementos na lista.

---

## `range()`

O comando:

```python
range(4)
```

representa:

```text
0, 1, 2, 3
```

O número final não é incluído.

Portanto:

```python
range(4)
```

não chega ao número `4`.

---

## Relação entre `len()` e `range()`

Considere:

```python
nomes = ["Raphael", "Lucas", "Ana"]
```

Temos:

```python
len(nomes)
```

resultado:

```text
3
```

Então:

```python
range(len(nomes))
```

equivale a:

```python
range(3)
```

que produz:

```text
0, 1, 2
```

Esses números correspondem exatamente aos índices existentes na lista.

---

## `for`

Exemplo:

```python
for indice in range(len(nomes)):
    print(indice)
```

A variável `indice` recebe, a cada volta:

```text
0
1
2
```

Já:

```python
for indice in range(len(nomes)):
    print(nomes[indice])
```

utiliza cada índice para acessar um elemento da lista.

Resultado:

```text
Raphael
Lucas
Ana
```

### Avaliação

A saída dos códigos foi identificada corretamente.

Entretanto, esta questão também mostrou que ainda era necessário reforçar a compreensão do caminho:

```text
len()
  ↓
range()
  ↓
for
  ↓
índice
  ↓
elemento da lista
```

Esse ponto se tornou um dos principais conteúdos das aulas seguintes.

---

# Questão 6 — Aplicação dos fundamentos

**Pontuação:** 3,5 / 4,0

A última questão reuniu diferentes conhecimentos estudados durante o primeiro ciclo.

Foram avaliadas habilidades como:

* leitura de código;
* identificação de variáveis;
* compreensão de listas;
* utilização de índices;
* interpretação de `for`;
* interpretação de `range()`;
* compreensão do fluxo de execução;
* indentação.

### Avaliação

O raciocínio geral estava correto e demonstrou boa assimilação dos fundamentos.

Algumas explicações, entretanto, ainda apresentavam imprecisões sobre o funcionamento interno do `for`, do `range()` e dos índices.

---

# Resultado da Prova 01

## Nota final: 9,25 / 10

```text
Questão 1 → 1,00 / 1,00
Questão 2 → 1,00 / 1,00
Questão 3 → 1,00 / 1,00
Questão 4 → 0,75 / 1,00
Questão 5 → 2,00 / 2,00
Questão 6 → 3,50 / 4,00

TOTAL → 9,25 / 10
```

**Resultado:** Aprovado.

---

# Pontos consolidados

Ao final da prova, estavam bem compreendidos:

* conceito de variável;
* tipos básicos de dados;
* `print()`;
* `input()`;
* comparações;
* estruturas condicionais;
* criação de listas;
* acesso básico aos elementos de uma lista;
* leitura de códigos simples;
* identificação da saída de programas.

---

# Pontos que precisavam de reforço

Apesar da excelente nota, a prova mostrou que alguns conceitos ainda precisavam ser trabalhados com maior profundidade.

## 1. `range()`

Foi necessário reforçar que:

```python
range(4)
```

produz:

```text
0, 1, 2, 3
```

e não:

```text
0, 1, 2, 3, 4
```

O limite final não é incluído.

---

## 2. Relação entre `len()` e `range()`

Foi necessário consolidar o raciocínio:

```python
len(lista)
```

descobre a quantidade de elementos.

Enquanto:

```python
range(len(lista))
```

pode produzir os números correspondentes aos índices da lista.

---

## 3. Variável do `for`

Neste código:

```python
for indice in range(len(nomes)):
```

`indice` recebe um valor diferente a cada volta.

Exemplo:

```text
1ª volta → indice = 0
2ª volta → indice = 1
3ª volta → indice = 2
```

---

## 4. Acesso por índice

O código:

```python
nomes[indice]
```

não representa a lista inteira.

Ele utiliza o valor atual de `indice` para localizar um elemento específico.

Exemplo:

```text
indice = 0 → nomes[0] → "Raphael"
indice = 1 → nomes[1] → "Lucas"
indice = 2 → nomes[2] → "Ana"
```

---

# Diagnóstico após a Prova 01

A Prova 01 mostrou um bom domínio dos fundamentos iniciais de Python.

A nota de **9,25 / 10** demonstrou que os conceitos básicos estavam sendo assimilados rapidamente.

Entretanto, a avaliação também revelou uma diferença importante entre:

```text
saber prever o resultado de um código
```

e:

```text
compreender exatamente como o Python chegou ao resultado
```

Principalmente em códigos envolvendo:

```python
for
range()
len()
```

Ainda havia dúvidas sobre o papel desempenhado por cada elemento.

Por isso, as aulas seguintes passaram a trabalhar com maior profundidade:

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
elemento
```

Posteriormente, esse conhecimento também passou a ser combinado com funções.

---

# Evolução esperada para a próxima prova

O objetivo após a Prova 01 passou a ser sair de uma compreensão predominantemente baseada na leitura da saída para uma compreensão completa do fluxo do programa.

Isso significa conseguir explicar:

```python
for indice in range(len(lista)):
    print(lista[indice])
```

não apenas dizendo qual será o resultado, mas compreendendo:

1. o que `len()` calcula;
2. o que `range()` produz;
3. quais valores `indice` recebe;
4. como o índice localiza um elemento;
5. por que o `for` repete o processo;
6. quando o laço termina.

Esse conhecimento formou a base para o ciclo seguinte do curso.
