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