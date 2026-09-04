# Prova 02 — Fundamentos de Python

**Nota:** 8,2 / 10
**Questões:** 10

---

## Objetivo da prova

Esta prova teve como objetivo avaliar a consolidação dos fundamentos estudados nas últimas aulas, principalmente:

* variáveis;
* tipos de dados (`str`, `int` e `float`);
* `print()`;
* listas;
* índices;
* `len()`;
* `range()`;
* `for`;
* funções;
* parâmetros e argumentos;
* combinação de listas, índices e funções;
* leitura e correção de códigos.

---

# Questão 1 — Fundamentos

## a) O que é uma variável em Python?

**Resposta:**

É um espaço virtual que pode receber e guardar valores, que vão sendo atualizados.

## b) Qual é a diferença entre uma `str`, um `int` e um `float`?

**Resposta:**

* `str`: significa que o dado é um texto.
* `int`: significa que o dado é um número inteiro e pode ser utilizado em cálculos.
* `float`: significa que o dado é um número decimal e também pode ser utilizado em cálculos.

## c) Para que serve a função `print()`?

**Resposta:**

Serve para mostrar na tela uma informação, uma lista, um dado ou um resultado.

## d) O que é uma lista?

**Resposta:**

É um espaço na memória capaz de armazenar uma série de dados.

### Avaliação

Fundamentos compreendidos.

**Observação:** uma lista armazena vários **elementos ou valores**.

---

# Questão 2 — Listas e índices

Código analisado:

```python
produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento"]

print(produtos[0])
print(produtos[2])
```

## Respostas

A saída será:

```text
SmartPOS
Link de Pagamento
```

Os números `0` e `2` representam os índices utilizados para localizar elementos dentro da lista.

Para acessar `"Tap to Phone"`:

```python
print(produtos[1])
```

A lista possui três elementos.

Para descobrir essa quantidade:

```python
len(produtos)
```

### Avaliação

Compreensão consolidada de listas, índices e `len()`.

---

# Questão 3 — `len()`, `range()` e `for`

Código analisado:

```python
vendas = [120, 85, 150, 200]

for indice in range(len(vendas)):
    print(indice, vendas[indice])
```

## Respostas

```python
len(vendas)
```

retorna:

```text
4
```

O `range()` produz:

```text
0, 1, 2, 3
```

Na primeira volta:

```text
indice = 0
vendas[indice] = 120
```

Na última volta:

```text
indice = 3
vendas[indice] = 200
```

Saída:

```text
0 120
1 85
2 150
3 200
```

### Avaliação

Excelente compreensão da relação entre `len()`, `range()`, índices e listas.

---

# Questão 4 — Funções, parâmetros e argumentos

Código analisado:

```python
def apresentar_produto(produto, preco):
    print("Produto:", produto)
    print("Preço:", preco)

apresentar_produto("SmartPOS", 150)
apresentar_produto("Tap to Phone", 90)
```

## Aprendizado principal

Na definição:

```python
def apresentar_produto(produto, preco):
```

`produto` e `preco` são **parâmetros**.

Na chamada:

```python
apresentar_produto("SmartPOS", 150)
```

`"SmartPOS"` e `150` são **argumentos**.

Uma forma simples de lembrar:

> Parâmetro é aquilo que a função está preparada para receber. Argumento é o valor que efetivamente enviamos quando chamamos a função.

Exemplo:

```text
produto  ← "SmartPOS"
preco    ← 150

parâmetro   argumento
```

### Ponto de atenção

A diferença entre **parâmetro e argumento** ainda precisa de reforço.

---

# Questão 5 — Listas + índices + função

Código:

```python
produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento"]
quantidades = [120, 85, 200]

def mostrar_venda(produto, quantidade):
    print(produto, "-", quantidade)

for indice in range(len(produtos)):
    mostrar_venda(produtos[indice], quantidades[indice])
```

## Aprendizado

As listas são:

```python
produtos
quantidades
```

Os parâmetros são:

```python
produto
quantidade
```

Na primeira volta:

```text
indice = 0
produtos[indice] = "SmartPOS"
quantidades[indice] = 120
```

A função recebe:

```text
produto = "SmartPOS"
quantidade = 120
```

O mesmo índice permite acessar elementos correspondentes das duas listas.

Saída:

```text
SmartPOS - 120
Tap to Phone - 85
Link de Pagamento - 200
```

### Avaliação

Excelente compreensão da combinação entre listas paralelas, índices e funções.

---

# Questão 6 — Construção de código

Código desenvolvido:

```python
projeto = ["Tap to Phone", "Link de Pagamento", "SmartPOS"]
responsavel = ["Ana", "Carlos", "Marina"]
progresso = [80, 60, 95]

def acompanhamento_projetos(projeto, responsavel, progresso):
    print("Projeto: ", projeto)
    print("Responsável: ", responsável)
    print("Progresso: ", progresso)

for indice in range(len(projeto)):
    acompanhamento_projetos(
        projeto[indice],
        responsavel[indice],
        progresso[indice]
    )
```

## Erro identificado

O parâmetro foi criado como:

```python
responsavel
```

mas dentro da função foi utilizado:

```python
responsável
```

Python considera esses nomes diferentes.

## Correção

```python
def acompanhamento_projetos(projeto, responsavel, progresso):
    print("Projeto:", projeto)
    print("Responsável:", responsavel)
    print("Progresso:", progresso)
```

### Avaliação

A lógica do programa estava correta. O erro foi de consistência na escrita do nome da variável.

---

# Questão 7 — Identificação e correção de erros

Nesta questão, os erros foram identificados corretamente durante a análise, mas alguns deles voltaram a aparecer ao reescrever o código completo.

## Código correto

```python
funcionarios = ["Ana", "Carlos", "Marina"]
salarios = [4500, 5200, 6100]

def mostrar_funcionario(funcionario, salario):
    print("Funcionário:", funcionario)
    print("Salário:", salario)

for indice in range(len(funcionarios)):
    mostrar_funcionario(funcionarios[indice], salarios[indice])
```

## Aprendizado

É importante revisar o código depois de escrevê-lo, verificando:

* se `def` termina com `:`;
* se os nomes utilizados são iguais aos nomes definidos;
* se uma variável representa uma lista ou apenas um elemento;
* se os argumentos enviados para a função estão corretos.

### Avaliação

A lógica foi compreendida, mas é necessário melhorar a revisão do código antes da execução.

---

# Questão 8 — Compreensão do fluxo

Código:

```python
setores = ["Comercial", "Produtos", "Tecnologia"]
demandas = [12, 8, 15]

def exibir_dados(setor, quantidade):
    print("Setor:", setor)
    print("Demandas:", quantidade)

for indice in range(len(setores)):
    setor_atual = setores[indice]
    quantidade_atual = demandas[indice]

    exibir_dados(setor_atual, quantidade_atual)
```

Na segunda volta:

```text
indice = 1
setor_atual = "Produtos"
quantidade_atual = 8
```

A função recebe:

```text
setor = "Produtos"
quantidade = 8
```

## Diferenças importantes

`setores` é uma lista.

`setor_atual` é uma variável que recebe um elemento da lista a cada volta.

`setor` é um parâmetro da função.

`"Produtos"` é um valor ou elemento armazenado na lista.

### Avaliação

Boa compreensão do caminho percorrido pelo dado dentro do programa.

---

# Questão 9 — Dois `for` e listas paralelas

Código problemático:

```python
for produto in produtos:
    for quantidade in quantidades:
        mostrar_venda(produto, quantidade)
```

Esse código combina cada produto com todas as quantidades.

Como existem três produtos e três quantidades:

```text
3 × 3 = 9
```

São realizadas nove chamadas da função.

Para relacionar os elementos pela posição:

```python
for indice in range(len(produtos)):
    mostrar_venda(produtos[indice], quantidades[indice])
```

Assim:

```text
produtos[0] ↔ quantidades[0]
produtos[1] ↔ quantidades[1]
produtos[2] ↔ quantidades[2]
```

### Avaliação

Excelente compreensão do motivo pelo qual utilizamos índices para relacionar listas paralelas.

---

# Questão 10 — Desafio final

Código desenvolvido:

```python
produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento"]
vendas = [180, 250, 140]
metas = [200, 220, 150]

def mostrar_resultado(produto, venda, meta)
    print("Produto: ", produto)
    print("Vendas: ", venda)
    print("Meta: ", meta)

for indice in range(len(produtos)):
    mostrar_resultados(produtos[indice], vendas[indice], metas[indice])
```

## Erro 1 — Dois pontos

Foi escrito:

```python
def mostrar_resultado(produto, venda, meta)
```

O correto é:

```python
def mostrar_resultado(produto, venda, meta):
```

## Erro 2 — Nome da função

A função foi definida como:

```python
mostrar_resultado
```

mas chamada como:

```python
mostrar_resultados
```

Python considera esses nomes diferentes.

## Código corrigido

```python
produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento"]
vendas = [180, 250, 140]
metas = [200, 220, 150]

def mostrar_resultado(produto, venda, meta):
    print("Produto:", produto)
    print("Vendas:", venda)
    print("Meta:", meta)

for indice in range(len(produtos)):
    mostrar_resultado(
        produtos[indice],
        vendas[indice],
        metas[indice]
    )
```

---

# Resultado

## Nota final: 8,2 / 10

A prova demonstrou que a lógica principal trabalhada durante este ciclo foi compreendida.

O fluxo:

```text
LISTA
  ↓
len()
  ↓
range()
  ↓
for
  ↓
índice
  ↓
elemento da lista
  ↓
argumento enviado
  ↓
parâmetro da função
  ↓
execução
```

está suficientemente consolidado para avançar no curso.

---

# Pontos consolidados

* criação e utilização de variáveis;
* tipos básicos;
* criação de listas;
* acesso por índices;
* funcionamento de `len()`;
* funcionamento de `range()`;
* utilização de `for`;
* leitura do fluxo de execução;
* criação básica de funções;
* passagem de valores para funções;
* utilização de índices em listas paralelas;
* combinação de `for`, `range()`, `len()`, listas e funções.

---

# Pontos para reforçar

## 1. Parâmetro x argumento

```python
def exemplo(parametro):
    print(parametro)

exemplo("argumento")
```

O parâmetro recebe.

O argumento é enviado.

---

## 2. Consistência nos nomes

Python diferencia:

```python
salario
salarios
```

e:

```python
mostrar_resultado
mostrar_resultados
```

Por isso, os nomes precisam ser escritos exatamente da mesma forma.

---

## 3. Sintaxe

Especial atenção aos dois pontos:

```python
def funcao():
```

e:

```python
for item in lista:
```

---

## 4. Revisão antes de executar

Antes de executar um código, verificar:

1. Os `:` estão presentes?
2. Os nomes das variáveis estão escritos da mesma forma?
3. Estou utilizando a lista correta?
4. A função chamada possui exatamente o mesmo nome da função criada?
5. Os argumentos estão na ordem correta?

---

# Diagnóstico para o próximo ciclo

A principal evolução deste ciclo foi a compreensão da relação entre:

```text
listas + índices + for + range() + len() + funções
```

Nas aulas anteriores, essa combinação ainda exigia reforço.

Na prova, ficou demonstrado que a lógica está suficientemente compreendida para avançar.

O próximo ciclo pode introduzir novos conteúdos voltados gradualmente para **Python aplicado à análise e ciência de dados**, mantendo pequenos exercícios de reforço sobre:

* parâmetros e argumentos;
* precisão na escrita;
* revisão e depuração de código.

O objetivo agora é transformar uma lógica já compreendida em código cada vez mais preciso e confiável.
