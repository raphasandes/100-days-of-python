"""Dia 13 — Desafio final: corrigir sintaxe e respeitar a condição pedida."""

produtos = [
    {"nome": "SmartPOS", "vendas": 150},
    {"nome": "Tap to Phone", "vendas": 250},
]

# O enunciado pede produtos com 200 vendas OU MAIS.
# Portanto, usamos >= (maior ou igual), e não apenas >.
for produto in produtos:
    if produto["vendas"] >= 200:
        print("Produto:", produto["nome"])

# Saída esperada:
# Produto: Tap to Phone
