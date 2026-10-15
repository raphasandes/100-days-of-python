"""Dia 13 — Exercícios corrigidos de revisão dos fundamentos."""


def exercicio_1_interpretacao():
    """Calcular diferenças entre vendas e metas e classificar produtos."""
    produtos = [
        {"nome": "SmartPOS", "vendas": 180, "meta": 200},
        {"nome": "Tap to Phone", "vendas": 250, "meta": 220},
        {"nome": "Link de Pagamento", "vendas": 140, "meta": 150},
    ]

    for produto in produtos:
        diferenca = produto["vendas"] - produto["meta"]
        if diferenca >= 0:
            status = "Meta atingida"
        else:
            status = "Abaixo da meta"
        print(produto["nome"], diferenca, status)


def exercicio_2_indices_e_chaves():
    """Mostrar como acessar dicionários e seus valores dentro de uma lista."""
    produtos = [
        {"nome": "SmartPOS", "vendas": 180},
        {"nome": "Tap to Phone", "vendas": 250},
    ]

    print("Segundo dicionário:", produtos[1])
    print("Vendas do segundo produto:", produtos[1]["vendas"])
    print("Nome do primeiro produto:", produtos[0]["nome"])


def exercicio_3_consolidacao():
    """Analisar metas e imprimir um relatório por produto."""
    produtos = [
        {"nome": "SmartPOS", "vendas": 320, "meta": 300},
        {"nome": "Tap to Phone", "vendas": 270, "meta": 300},
        {"nome": "Link de Pagamento", "vendas": 190, "meta": 180},
    ]

    for produto in produtos:
        diferenca = produto["vendas"] - produto["meta"]

        if diferenca >= 0:
            status = "Meta atingida"
        else:
            status = "Não atingiu a meta"

        print("Produto:", produto["nome"])
        print("Diferença:", diferenca)
        print("Status:", status)
        print("--------------------")


def exercicio_4_construcao_guiada():
    """Exibir somente produtos com vendas estritamente maiores que 120."""
    produtos = [
        {"nome": "SmartPOS", "vendas": 150},
        {"nome": "Tap to Phone", "vendas": 250},
        {"nome": "Link de Pagamento", "vendas": 100},
    ]

    for produto in produtos:
        if produto["vendas"] > 120:
            print(produto["nome"])


if __name__ == "__main__":
    print("=== EXERCÍCIO 1 — INTERPRETAÇÃO ===")
    exercicio_1_interpretacao()
    print("\n=== EXERCÍCIO 2 — ÍNDICES E CHAVES ===")
    exercicio_2_indices_e_chaves()
    print("\n=== EXERCÍCIO 3 — CONSOLIDAÇÃO ===")
    exercicio_3_consolidacao()
    print("\n=== EXERCÍCIO 4 — CONSTRUÇÃO GUIADA ===")
    exercicio_4_construcao_guiada()
