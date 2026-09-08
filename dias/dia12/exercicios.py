
### `exercicios.py`

```python
# Aula 12 — Percorrendo listas de dicionários com for


# ----------------------------------------
# Base de dados utilizada nos exercícios
# ----------------------------------------

produtos = [
    {
        "nome": "SmartPOS",
        "vendas": 180,
        "meta": 200
    },
    {
        "nome": "Tap to Phone",
        "vendas": 250,
        "meta": 220
    },
    {
        "nome": "Link de Pagamento",
        "vendas": 140,
        "meta": 150
    }
]


# ----------------------------------------
# Exercício 1 — Acessando os dicionários
# ----------------------------------------

print(produtos[0])

print(produtos[2]["nome"])

print(produtos[1]["meta"])


# ----------------------------------------
# Exercício 2 — Percorrendo diretamente
# ----------------------------------------

for produto in produtos:
    print(produto)


# ----------------------------------------
# Exercício 3 — Acessando uma chave
# ----------------------------------------

for produto in produtos:
    print(produto["nome"])


# ----------------------------------------
# Exercício 4 — Exibindo vendas
# ----------------------------------------

for produto in produtos:
    print(produto["vendas"])


# ----------------------------------------
# Exercício 5 — Nome e vendas
# ----------------------------------------

for produto in produtos:
    print("Produto:", produto["nome"])
    print("Vendas:", produto["vendas"])


# ----------------------------------------
# Exercício 6 — Verificando a meta
# ----------------------------------------

for produto in produtos:
    if produto["vendas"] >= produto["meta"]:
        print(produto["nome"], "atingiu a meta")


# ----------------------------------------
# Exercício 7 — Calculando a diferença
# ----------------------------------------

for produto in produtos:
    diferenca = produto["vendas"] - produto["meta"]

    print(produto["nome"], diferenca)