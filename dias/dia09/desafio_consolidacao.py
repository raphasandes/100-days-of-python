# Dia 09 — Desafio de Consolidação
# Funções, listas, índices, for, range() e len()

produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento", "Pix no POS"]
quantidade = [185, 92, 143, 76]


def consolidacao(produto, cliente):
    print("Produto:", produto)
    print("Clientes ativos:", cliente)
    print()


for indice in range(len(produtos)):
    consolidacao(produtos[indice], quantidade[indice])