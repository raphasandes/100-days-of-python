# Dia 06 — Prova 1

## Objetivo

Primeira avaliação do curso de Python, reunindo os conteúdos estudados nas cinco primeiras aulas.

## Conteúdos avaliados

- Variáveis
- Tipos de dados
- `print()`
- Condicionais
- Listas
- Índices
- `len()`
- Laços de repetição com `for`
- `range()`
- Indentação

---

# Resultado

**Nota final:** 9,25 / 10,00

**Situação:** ✅ Aprovado

---

# Questão 1 — Variáveis e tipos de dados

## Enunciado

Analise o código:

```python
nome = "Raphael"
idade = 34

print(nome)
print(idade)
```

Responda:

1. Qual será a saída completa?
2. Que tipo de dado é `nome`?
3. Que tipo de dado é `idade`?

## Minha resposta

> Qual será a saída completa?

```text
Raphael
34
```

> Que tipo de dado é `nome`?

String, pois o valor aparece entre aspas.

> Que tipo de dado é `idade`?

Integer, pois é um número inteiro.

## Correção

✅ A saída foi identificada corretamente.

✅ `nome` é uma string.

Em Python, o nome técnico desse tipo é:

```python
str
```

✅ `idade` é um número inteiro.

Em Python, o nome técnico desse tipo é:

```python
int
```

### Ajuste de escrita

A palavra correta em inglês é `integer`, e não `interger`.

**Nota: 1,0 / 1,0**

---

# Questão 2 — Condicionais

## Enunciado

Analise o código:

```python
temperatura = 18

if temperatura > 25:
    print("Quente")
else:
    print("Frio")
```

Responda:

1. O que será impresso?
2. Por que o Python entrou nesse bloco e não no outro?

## Minha resposta

> O que será impresso?

```text
Frio
```

> Por que o Python entrou nesse bloco e não no outro?

Como a primeira condição não foi atendida, pois a temperatura não é maior que 25, o Python seguiu para o próximo comando e imprimiu `"Frio"`.

## Correção

✅ A saída foi identificada corretamente.

A condição:

```python
18 > 25
```

é falsa.

Por isso, o Python ignora o bloco do `if` e executa o bloco do `else`.

### Ajuste de precisão

Não é apenas o "próximo comando". O Python executa especificamente o bloco `else`, porque a condição do `if` foi avaliada como falsa.

**Nota: 1,0 / 1,0**

---

# Questão 3 — Listas, índices e `len()`

## Enunciado

Analise o código:

```python
nomes = ["Raphael", "Lucas", "Ana"]

print(nomes[1])
print(len(nomes))
```

Responda:

1. O que será impresso na primeira linha?
2. O que será impresso na segunda linha?
3. Por que `nomes[1]` não imprime `"Raphael"`?
4. O que aconteceria com `print(nomes[3])`?

## Minha resposta

> O que será impresso na primeira linha?

```text
Lucas
```

> O que será impresso na segunda linha?

```text
3
```

Acredito que `len()` mostra o tamanho da lista.

> Por que `nomes[1]` não imprime `"Raphael"`?

Porque a contagem dos valores de uma lista começa em zero no Python. O valor de índice zero está a zero passos do início da lista.

> O que aconteceria com `print(nomes[3])`?

Apareceria uma mensagem de erro, pois não existe valor armazenado na quarta posição.

## Correção

✅ `nomes[1]` imprime:

```text
Lucas
```

✅ `len(nomes)` retorna:

```text
3
```

A função `len()` informa a quantidade de elementos da lista.

Os índices são:

```text
0 → Raphael
1 → Lucas
2 → Ana
```

✅ `nomes[3]` provoca um erro, pois esse índice não existe.

O erro é:

```text
IndexError: list index out of range
```

**Nota: 1,0 / 1,0**

---

# Questão 4 — `for` e `range()`

## Enunciado

Analise o código:

```python
for numero in range(4):
    print(numero)
```

Responda:

1. Qual será a saída completa?
2. Quais valores a variável `numero` assume?
3. Por que o número 4 não aparece?

## Minha resposta

> Qual será a saída completa?

```text
0
1
2
3
```

> Quais valores a variável `numero` assume?

Ela assume os números de zero a três.

> Por que o número 4 não aparece?

Porque a contagem é iniciada no número zero.

## Correção

✅ A saída foi identificada corretamente.

✅ A variável `numero` recebe:

```text
0
1
2
3
```

🟡 A explicação sobre o número 4 estava parcialmente correta.

O fato de a contagem começar em zero ajuda a compreender a sequência, mas o motivo principal é que:

```python
range(4)
```

gera números de zero até **antes do limite 4**.

O valor final do `range()` não é incluído.

**Nota: 0,75 / 1,0**

---

# Questão 5 — Condições e indentação

## Enunciado

Analise o código:

```python
cooperativa = "Planalto Central"
faturamento = 25000

if faturamento >= 20000:
    print(cooperativa)
    print("Meta atingida!")
else:
    print("Meta não atingida.")
```

Responda:

1. O que será impresso?
2. Por que `"Meta atingida!"` será exibida?
3. Se o faturamento fosse `18000`, qual seria a saída?
4. O nome da cooperativa apareceria nesse segundo caso?

## Minha resposta

> O que será impresso?

```text
Planalto Central
Meta atingida!
```

> Por que `"Meta atingida!"` será exibida?

Porque a condição foi atendida:

```text
25000 >= 20000
```

> Se o faturamento fosse `18000`, qual seria a saída?

```text
Meta não atingida.
```

> O nome da cooperativa apareceria?

Não apareceria, porque `print(cooperativa)` está indentado dentro da primeira condição.

## Correção

✅ Todas as respostas estavam corretas.

A condição:

```python
25000 >= 20000
```

é verdadeira. Portanto, o bloco do `if` é executado.

Com faturamento de `18000`, a condição seria falsa e o Python executaria apenas o bloco do `else`.

A explicação sobre indentação foi precisa: o nome da cooperativa só é exibido quando o bloco do `if` é executado.

**Nota: 2,0 / 2,0**

---

# Questão 6 — Desafio final

## Enunciado

Analise o código:

```python
nomes = ["Raphael", "Lucas", "Ana"]

for indice in range(len(nomes)):
    print(indice, "-", nomes[indice])
```

Responda:

1. Qual será a saída completa?
2. O que `len(nomes)` retorna?
3. Quais valores a variável `indice` assume?
4. Por que usamos `nomes[indice]` em vez de apenas `nomes`?

## Minha resposta

> Qual será a saída completa?

```text
0 - Raphael
1 - Lucas
2 - Ana
```

> O que `len(nomes)` retorna?

Ela registra o tamanho da lista. Nesse caso, o resultado é `3`.

> Quais valores a variável `indice` assume?

Ela recebe temporariamente os valores de `len(nomes)` e é atualizada a cada repetição do laço.

> Por que usamos `nomes[indice]`?

Eu não sabia exatamente. Minha hipótese foi que isso criava uma ordem lógica conectando o índice e o nome, fazendo com que aparecessem em ordem.

## Correção

✅ A saída foi identificada corretamente.

✅ `len(nomes)` retorna:

```text
3
```

### Ajuste de vocabulário

A função `len()` não "registra" o tamanho. Ela **retorna** o tamanho da lista.

🟡 A explicação sobre a variável `indice` estava parcialmente correta.

O fluxo é:

```text
len(nomes)
↓
3
↓
range(3)
↓
0, 1, 2
↓
indice
```

A variável `indice` não recebe diretamente o valor `3`. Ela recebe, uma vez por repetição:

```text
0
1
2
```

🟡 A explicação sobre `nomes[indice]` apresentou uma boa intuição.

`nomes[indice]` permite acessar um elemento específico da lista em cada repetição:

```text
nomes[0] → Raphael
nomes[1] → Lucas
nomes[2] → Ana
```

Se fosse usado apenas:

```python
print(nomes)
```

a lista inteira seria impressa em todas as repetições.

**Nota: 3,5 / 4,0**

---

# Resultado final detalhado

| Questão | Conteúdo | Nota |
|---|---|---:|
| 1 | Variáveis e tipos | 1,00 |
| 2 | Condicionais | 1,00 |
| 3 | Listas, índices e `len()` | 1,00 |
| 4 | `for` e `range()` | 0,75 |
| 5 | Condições e indentação | 2,00 |
| 6 | Listas, índices e repetição | 3,50 |
|  | **Nota final** | **9,25 / 10,00** |

---

# Feedback final

## Pontos fortes

- Boa capacidade de prever a saída de códigos.
- Compreensão consistente de variáveis e tipos.
- Bom entendimento de listas e índices.
- Excelente interpretação de condicionais.
- Excelente compreensão da importância da indentação.
- Capacidade de explicar o próprio raciocínio.
- Honestidade ao indicar dúvidas durante a resolução.

## Pontos para revisar

- Funcionamento exato do `range()`.
- Diferença entre limite final e valores gerados.
- Fluxo de execução de um laço `for`.
- Relação entre `len()`, `range()` e índices.
- Diferença entre uma lista inteira e um elemento da lista.

---

# Reflexão pessoal

Esta foi minha primeira prova de Python.

Percebi que já consigo interpretar códigos e prever seus resultados com boa segurança. Meu melhor desempenho apareceu nas questões sobre condicionais, listas e indentação.

Também identifiquei que ainda preciso visualizar melhor o fluxo de execução dos laços de repetição. Minha principal dificuldade está em compreender, passo a passo, como `len()`, `range()` e os índices trabalham juntos.

Na próxima aula, revisarei esses pontos antes de iniciar o próximo conteúdo.

---

# Próxima etapa

- Revisar `range()`.
- Revisar listas e índices.
- Revisar o fluxo de execução do `for`.
- Iniciar o próximo módulo do curso.