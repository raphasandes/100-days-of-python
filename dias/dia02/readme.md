# Dia 02 — Estruturas condicionais

## Objetivo

Aprender a criar programas capazes de tomar decisões com base em condições.

---

# Conteúdos estudados

- `if`
- `elif`
- `else`
- Operadores de comparação
- Indentação
- Diferença entre atribuição e comparação
- Condições verdadeiras e falsas

---

# Exercícios desenvolvidos

## Temperatura

```python
temperatura = 31

if temperatura > 25:
    print("Quente")
else:
    print("Frio")
```

A condição:

```python
temperatura > 25
```

é verdadeira. Por isso, o programa imprime:

```text
Quente
```

---

## Frete grátis

```python
valor_compra = 250

if valor_compra >= 200:
    print("Frete grátis")
else:
    print("Frete não gratuito")
```

O operador `>=` significa **maior ou igual a**.

---

## Maioridade

```python
idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

Como `16 >= 18` é falso, o bloco do `else` é executado.

---

## Uso do `elif`

```python
temperatura = 20

if temperatura > 25:
    print("Quente")
elif temperatura >= 15:
    print("Agradável")
else:
    print("Frio")
```

O `elif` permite verificar uma nova condição quando a primeira não é atendida.

---

# Conceitos importantes

## `if`

Executa um bloco quando a condição é verdadeira.

```python
if idade >= 18:
    print("Maior de idade")
```

## `else`

Executa um bloco quando a condição do `if` é falsa.

```python
else:
    print("Menor de idade")
```

## `elif`

Adiciona uma nova condição entre o `if` e o `else`.

```python
elif temperatura >= 15:
    print("Agradável")
```

## Atribuição x comparação

O sinal `=` atribui um valor:

```python
idade = 16
```

O operador `==` compara dois valores:

```python
idade == 16
```

## Operadores estudados

| Operador | Significado |
|---|---|
| `>` | Maior que |
| `<` | Menor que |
| `>=` | Maior ou igual a |
| `<=` | Menor ou igual a |
| `==` | Igual a |
| `!=` | Diferente de |

---

# O que aprendi

Aprendi que um programa pode tomar decisões de acordo com regras definidas no código.

Também compreendi que o Python avalia condições como verdadeiras ou falsas e executa apenas o bloco correspondente.

A indentação é essencial, pois determina quais comandos pertencem ao `if`, ao `elif` ou ao `else`.

---

# Aplicação prática

Estruturas condicionais podem ser utilizadas para representar regras de negócio, como:

- aprovação de uma transação;
- alcance de uma meta;
- elegibilidade para uma campanha;
- concessão de frete grátis;
- classificação de resultados.

---

# Evolução

## O que eu ainda não sabia antes

- Como fazer um programa tomar decisões.
- A diferença entre `=` e `==`.
- Como utilizar `if`, `elif` e `else`.
- A importância da indentação.

## O que sei fazer hoje

- Criar condições.
- Comparar valores.
- Executar códigos diferentes conforme uma regra.
- Representar regras simples de negócio.

---

# Para revisar antes da próxima aula

- [ ] Diferença entre `=` e `==`.
- [ ] Operadores de comparação.
- [ ] Funcionamento de `if`, `elif` e `else`.
- [ ] Importância da indentação.

---

# Arquivos desta aula

| Arquivo | Descrição |
|---|---|
| `exercicio.py` | Exercícios de estruturas condicionais. |
| `README.md` | Documentação técnica da aula. |
| `reflexao.md` | Reflexão pessoal sobre o aprendizado. |