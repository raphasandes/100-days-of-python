# Dia 03 — Listas e índices

## Objetivo

Aprender a armazenar vários valores em uma única variável e acessar elementos específicos por meio de índices.

---

# Conteúdos estudados

- Listas
- Índices
- `len()`
- Valores booleanos
- `True`
- `False`

---

# Exercício desenvolvido

```python
nomes = ["Raphael", "Lucas", "Ana"]

print(nomes)
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(len(nomes))
```

Saída:

```text
['Raphael', 'Lucas', 'Ana']
Raphael
Lucas
Ana
3
```

---

# Conceitos importantes

## Lista

Uma lista permite armazenar vários valores dentro de uma única variável.

```python
nomes = ["Raphael", "Lucas", "Ana"]
```

## Índices

Os índices começam em zero:

```text
0 → Raphael
1 → Lucas
2 → Ana
```

Por isso:

```python
print(nomes[1])
```

imprime:

```text
Lucas
```

## `len()`

A função `len()` retorna a quantidade de elementos.

```python
print(len(nomes))
```

Resultado:

```text
3
```

## Valores booleanos

Valores booleanos representam verdadeiro ou falso:

```python
meta_atingida = True
estabelecimento_ativo = False
```

O tipo desses valores é:

```python
bool
```

---

# Erro de índice

A lista possui três elementos, mas os índices disponíveis são:

```text
0
1
2
```

O código:

```python
print(nomes[3])
```

causaria:

```text
IndexError: list index out of range
```

---

# O que aprendi

Aprendi que listas são úteis quando precisamos armazenar vários valores relacionados.

Também compreendi que o Python começa a contar os índices a partir de zero.

A função `len()` permite descobrir a quantidade de elementos sem precisar contá-los manualmente.

---

# Aplicação prática

Listas podem armazenar:

- estabelecimentos comerciais;
- cooperativas;
- bandeiras;
- produtos;
- transações;
- responsáveis por projetos;
- resultados mensais.

Isso evita a criação de uma variável diferente para cada informação.

---

# Evolução

## O que eu ainda não sabia antes

- Como armazenar vários valores em uma variável.
- Que os índices começam em zero.
- Como acessar um elemento específico.
- Como descobrir o tamanho de uma lista.
- O que são valores booleanos.

## O que sei fazer hoje

- Criar listas.
- Acessar elementos com índices.
- Utilizar `len()`.
- Identificar índices inexistentes.
- Trabalhar com `True` e `False`.

---

# Para revisar antes da próxima aula

- [ ] Índices iniciados em zero.
- [ ] Diferença entre tamanho e último índice.
- [ ] Uso de `len()`.
- [ ] Diferença entre a lista inteira e um elemento.

---

# Arquivos desta aula

| Arquivo | Descrição |
|---|---|
| `exercicio.py` | Exercícios com listas, índices e booleanos. |
| `README.md` | Documentação técnica da aula. |
| `reflexao.md` | Reflexão pessoal sobre o aprendizado. |