# Aula 12 — Desafio
# Análise de desempenho dos produtos


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


# Percorrer todos os produtos
for produto in produtos:

    # Calcular a diferença entre vendas e meta
    diferenca = produto["vendas"] - produto["meta"]

    # Analisar o desempenho do produto
    if diferenca >= 0:
        print(produto["nome"], "acima da meta")
    else:
        print(produto["nome"], "abaixo da meta")