# Dia 07 — Mini-projeto
# Gerador de Relatórios
#
# Todos os nomes, dados e cenários deste programa são fictícios
# e foram criados exclusivamente para fins educacionais.


def linha():
    print("========================================")


def titulo(texto):
    linha()
    print(texto)
    linha()


def relatorio_vendas():
    titulo("RELATÓRIO DE VENDAS")
    print()
    print("Clientes ativos: 185")
    print("Faturamento: R$ 250.000")


def relatorio_estoque():
    titulo("RELATÓRIO DE ESTOQUE")
    print()
    print("Produtos: 82")
    print("Itens em falta: 6")


def relatorio_financeiro():
    titulo("RELATÓRIO FINANCEIRO")
    print()
    print("Total em caixa: R$ 1.000.000,02")
    print("Entradas futuras: R$ 325.128,02")
    print("Despesas futuras: R$ 2,00")


relatorio_vendas()

print()

relatorio_estoque()

print()

relatorio_financeiro()