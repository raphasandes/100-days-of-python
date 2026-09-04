# Dia 10 — Desafio de construção autônoma
# Relatório de produtos


produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento"]
clientes = [185, 92, 143]
faturamentos = [250000, 98000, 175000]


print("RELATÓRIO DE PRODUTOS")
print("=========================")


def relatorio_produtos(produto, cliente, faturamento):
    print("Produto:", produto)
    print("Clientes ativos:", cliente)
    print("Faturamento: R$", faturamento)
    print("-------------------------")


for numero in range(len(produtos)):
    relatorio_produtos(
        produtos[numero],
        clientes[numero],
        faturamentos[numero]
    )