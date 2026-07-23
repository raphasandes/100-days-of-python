# Dia 04 — Revisão dos fundamentos

## Objetivo

Revisar e integrar os principais conteúdos estudados nas primeiras aulas.

---

# Conteúdos revisados

- Variáveis
- Strings
- Números inteiros
- Valores booleanos
- `print()`
- Condicionais
- Operadores de comparação
- Listas
- Índices
- `len()`
- Indentação

---

# Exercício desenvolvido

```python
nome = "Raphael"
idade = 34
estuda_python = True

print(nome)
print(idade)
print(estuda_python)
```

```python
temperatura = 18

if temperatura > 25:
    print("Quente")
else:
    print("Frio")
```

```python
nomes = ["Raphael", "Lucas", "Ana"]

print(nomes[0])
print(nomes[1])
print(nomes[2])
print(len(nomes))
```

```python
faturamento = 25000

if faturamento >= 20000:
    print("Meta atingida!")
else:
    print("Meta não atingida.")
```

---

# O que aprendi

A revisão ajudou a perceber que os conceitos não funcionam de maneira isolada.

Uma lista pode armazenar informações, uma variável pode guardar um valor utilizado em uma condição e o programa pode apresentar um resultado diferente conforme a regra definida.

Também pratiquei a leitura de código antes da execução, tentando prever os resultados.

---

# Integração dos conceitos

Um programa pode:

1. armazenar dados em variáveis;
2. organizar vários dados em listas;
3. acessar elementos com índices;
4. avaliar condições;
5. exibir resultados com `print()`.

Exemplo:

```python
cooperativas = ["Central", "Regional", "Nacional"]
faturamento = 25000

if faturamento >= 20000:
    print(cooperativas[0])
    print("Meta atingida!")
else:
    print("Meta não atingida.")
```

---

# Aplicação prática

A combinação desses conceitos permite começar a representar regras simples de negócio.

Exemplos:

- identificar se uma meta foi atingida;
- verificar a elegibilidade de um estabelecimento;
- acessar dados de uma cooperativa;
- apresentar mensagens conforme o resultado;
- organizar grupos de informações.

---

# Evolução

## O que eu ainda não sabia antes

- Como combinar variáveis, listas e condições.
- Como prever o resultado de um programa.
- Como a indentação interfere na execução.
- Como representar uma regra de negócio simples.

## O que sei fazer hoje

- Ler códigos simples.
- Prever resultados.
- Criar condições.
- Utilizar listas e índices.
- Combinar diferentes fundamentos em um programa.

---

# Para revisar antes da próxima aula

- [ ] Índices e `len()`.
- [ ] Operadores de comparação.
- [ ] Fluxo de execução do `if`.
- [ ] Indentação.
- [ ] Previsão da saída de códigos.

---

# Arquivos desta aula

| Arquivo | Descrição |
|---|---|
| `exercicio.py` | Exercícios de revisão dos fundamentos. |
| `README.md` | Documentação técnica da revisão. |
| `reflexao.md` | Reflexão pessoal sobre o aprendizado. |