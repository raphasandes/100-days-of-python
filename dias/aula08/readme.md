# Aula 08 — Revisão de Python

Esta aula foi dedicada à retomada dos estudos após uma pausa.

O objetivo foi revisar os principais conceitos estudados anteriormente e identificar quais conteúdos ainda precisam de reforço antes de avançar.

---

## Conteúdos revisados

- Variáveis
- Tipos de dados (`str` e `int`)
- `print()`
- Listas
- Índices
- `len()`
- Estruturas de repetição com `for`
- `range()`
- Funções com `def`
- Chamada de funções
- Parâmetros
- Argumentos
- Combinação de listas, repetições e funções

---

## 1. Variáveis e tipos de dados

Variáveis permitem armazenar valores que podem ser utilizados posteriormente pelo programa.

Exemplo:

```python
nome = "Raphael"
idade = 34

print(nome)
print(idade)
```

Neste exemplo:

- `nome` é uma variável que armazena uma `str`;
- `idade` é uma variável que armazena um `int`.

As aspas são importantes para identificar textos.

Existe diferença entre:

```python
print(nome)
```

e:

```python
print("nome")
```

No primeiro caso, o Python procura o valor armazenado na variável `nome`.

No segundo caso, o Python imprime literalmente o texto `"nome"`.

---

## 2. Listas

Listas permitem armazenar vários elementos dentro de uma mesma estrutura.

Exemplo:

```python
produtos = [
    "Débito",
    "Crédito",
    "Pix"
]
```

Podemos acessar individualmente os elementos utilizando seus índices:

```python
print(produtos[0])
print(produtos[1])
print(produtos[2])
```

Resultado:

```text
Débito
Crédito
Pix
```

---

## 3. Índices

Os índices de uma lista começam em `0`.

Para a lista:

```python
produtos = ["Débito", "Crédito", "Pix"]
```

temos:

```text
Índice 0 → Débito
Índice 1 → Crédito
Índice 2 → Pix
```

Por isso, uma lista com três elementos possui os índices `0`, `1` e `2`.

Tentar acessar:

```python
produtos[3]
```

gera um erro, pois esse índice não existe.

O erro é chamado de:

```text
IndexError: list index out of range
```

---

## 4. len()

A função `len()` informa a quantidade de elementos existentes em uma estrutura.

Exemplo:

```python
produtos = ["Débito", "Crédito", "Pix"]

print(len(produtos))
```

Resultado:

```text
3
```

É importante diferenciar:

```text
Quantidade de elementos → 3
Último índice           → 2
```

Isso acontece porque os índices começam em `0`.

---

## 5. Repetições com for

O `for` permite repetir um conjunto de comandos.

Também podemos utilizá-lo para percorrer os elementos de uma lista.

Exemplo:

```python
produtos = ["Débito", "Crédito", "Pix"]

for produto in produtos:
    print(produto)
```

Durante a execução:

```text
1ª volta → produto = "Débito"
2ª volta → produto = "Crédito"
3ª volta → produto = "Pix"
```

Resultado:

```text
Débito
Crédito
Pix
```

A variável `produto` recebe temporariamente cada elemento da lista.

---

## 6. range()

`range()` gera uma sequência de números.

Exemplo:

```python
for numero in range(3):
    print(numero)
```

Resultado:

```text
0
1
2
```

`range(3)` começa em `0` e termina antes de chegar ao número `3`.

Portanto:

```text
range(3) → 0, 1, 2
```

O `range()` não acessa diretamente os elementos de uma lista. Ele fornece números que podem, por exemplo, ser utilizados como índices.

---

## 7. Combinando range() e índices

Podemos utilizar os números gerados por `range()` para acessar posições de uma lista.

Exemplo:

```python
produtos = ["Débito", "Crédito", "Pix"]

for numero in range(3):
    print(produtos[numero])
```

Durante a execução:

```text
numero = 0 → produtos[0] → Débito
numero = 1 → produtos[1] → Crédito
numero = 2 → produtos[2] → Pix
```

Resultado:

```text
Débito
Crédito
Pix
```

---

## 8. Combinando range() e len()

Em vez de informar manualmente quantas vezes o `for` deverá executar, podemos utilizar `len()`.

Exemplo:

```python
for numero in range(len(produtos)):
    print(produtos[numero])
```

O processo pode ser entendido assim:

```text
produtos
    ↓
len(produtos)
    ↓
3
    ↓
range(3)
    ↓
0, 1, 2
    ↓
produtos[0]
produtos[1]
produtos[2]
```

Essa solução é melhor do que escrever:

```python
range(3)
```

porque o código se adapta automaticamente caso novos elementos sejam adicionados à lista.

Resumo:

```text
len()   → descobre quantos elementos existem
range() → gera uma sequência de números
```

---

## 9. Funções

Funções permitem agrupar comandos que poderão ser executados sempre que necessário.

Uma função é definida utilizando `def`.

Exemplo:

```python
def saudacao():
    print("Olá!")
    print("Bem-vindo ao sistema.")
```

Nesse momento, a função foi definida, mas seus comandos ainda não foram executados.

Para executar a função:

```python
saudacao()
```

Resultado:

```text
Olá!
Bem-vindo ao sistema.
```

Portanto:

```text
def saudacao(): → define a função
saudacao()      → chama/executa a função
```

Uma das vantagens das funções é evitar repetição de código.

Se uma função for utilizada várias vezes e precisar ser modificada posteriormente, podemos alterar apenas sua definição.

---

## 10. Parâmetros e argumentos

Uma função também pode receber informações.

Exemplo:

```python
def saudacao(nome):
    print("Olá,", nome)

saudacao("Ana")
```

Neste exemplo:

```text
nome  → parâmetro
"Ana" → argumento
```

O parâmetro aparece na definição da função.

O argumento é o valor enviado quando a função é chamada.

Durante a execução:

```text
nome recebe "Ana"
```

e o resultado será:

```text
Olá, Ana
```

---

## 11. Funções com mais de um parâmetro

Uma função pode receber vários parâmetros.

Exemplo:

```python
def apresentar_produto(produto, preco):
    print("Produto:", produto)
    print("Preço:", preco)

apresentar_produto("SmartPOS", 150)
```

Durante a chamada:

```text
produto recebe "SmartPOS"
preco recebe 150
```

Resultado:

```text
Produto: SmartPOS
Preço: 150
```

---

## 12. Combinando lista, for e função

Também podemos chamar uma função dentro de uma repetição.

Exemplo:

```python
def mostrar_produto(nome):
    print("Produto:", nome)

produtos = [
    "SmartPOS",
    "Tap to Phone",
    "Link de Pagamento"
]

for produto in produtos:
    mostrar_produto(produto)
```

A cada repetição, `produto` recebe um elemento da lista e esse valor é enviado como argumento para a função.

Resultado:

```text
Produto: SmartPOS
Produto: Tap to Phone
Produto: Link de Pagamento
```

---

## 13. Exercício da aula — Projetos em andamento

Durante a revisão, foi desenvolvido um exercício utilizando duas listas relacionadas.

```python
def projetos_andamento(projeto, status_pendente):
    print("Nome do Projeto:", projeto)
    print("Status:", status_pendente)
    print()

projetos = [
    "Tap to Phone",
    "Acordo de Incentivo",
    "Nova Política"
]

status_pendente = [
    "Sim",
    "Não",
    "Sim"
]

for numero in range(len(projetos)):
    projetos_andamento(
        projetos[numero],
        status_pendente[numero]
    )
```

As duas listas estão relacionadas pelos índices:

```text
projetos[0] → Tap to Phone
status_pendente[0] → Sim

projetos[1] → Acordo de Incentivo
status_pendente[1] → Não

projetos[2] → Nova Política
status_pendente[2] → Sim
```

O mesmo índice é utilizado para buscar as informações correspondentes nas duas listas.

---

## Principal aprendizado da aula

A revisão mostrou que os conceitos básicos estudados anteriormente foram recuperados.

Variáveis, tipos de dados, listas, índices, `len()` e conceitos básicos de funções apresentaram boa compreensão.

O principal ponto de atenção identificado foi a construção autônoma de programas que combinam diferentes estruturas.

É necessário reforçar principalmente:

- funções;
- parâmetros e argumentos;
- chamadas de funções;
- listas dentro de repetições;
- índices;
- `for`;
- `range()`;
- `len()`;
- combinação desses elementos em um mesmo programa.

Também foi identificado que é importante praticar a transformação de uma sequência de comandos manuais em uma estrutura automatizada utilizando repetição.

---

## Evolução

### O que já consigo fazer

- Criar variáveis.
- Trabalhar com `str` e `int`.
- Exibir informações utilizando `print()`.
- Criar listas.
- Acessar elementos utilizando índices.
- Utilizar `len()` para descobrir a quantidade de elementos.
- Compreender repetições utilizando `for`.
- Compreender o funcionamento básico de `range()`.
- Criar funções simples.
- Chamar funções.
- Compreender parâmetros e argumentos.
- Acompanhar a execução de uma função dentro de uma repetição.

### O que preciso reforçar

- Escrever funções de forma autônoma.
- Combinar funções e estruturas de repetição.
- Utilizar índices dentro de repetições.
- Utilizar `range()` e `len()` em conjunto.
- Relacionar elementos de listas diferentes por meio de seus índices.
- Transformar processos repetitivos em estruturas automatizadas.
- Construir programas completos utilizando vários conceitos simultaneamente.

---

## Próxima aula

A Aula 09 será uma aula de reforço.

O foco será principalmente em funções e na combinação das funções com conteúdos já estudados.

Serão praticados:

1. criação de funções;
2. chamada de funções;
3. parâmetros e argumentos;
4. funções com múltiplos parâmetros;
5. funções combinadas com listas;
6. funções dentro de estruturas de repetição;
7. uso de `for`, `range()` e `len()`;
8. construção autônoma de pequenos programas.

O objetivo será consolidar esses conhecimentos antes de avançar para novos conteúdos.