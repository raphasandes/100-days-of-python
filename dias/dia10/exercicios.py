
## `exercicio.py`

```python
# Dia 10 — Consolidação
# Funções + listas + índices + for + range() + len()


# Exercício 1 — Produtos e quantidades

produtos = ["SmartPOS", "Tap to Phone", "Pix no POS"]
quantidades = [185, 92, 76]


def mostrar_produto(produto, quantidade):
    print("Produto:", produto)
    print("Quantidade:", quantidade)


for numero in range(len(produtos)):
    mostrar_produto(produtos[numero], quantidades[numero])


print()


# Exercício 2 — Funcionários

funcionarios = ["Marcos", "Fernanda", "João"]
salarios = [3200, 4500, 3800]
setores = ["Vendas", "Financeiro", "Tecnologia"]


def mostrar_funcionario(nome, holerite, area):
    print("Funcionário:", nome)
    print("Salário: R$", holerite)
    print("Setor:", area)
    print("--------------------")


for numero in range(len(funcionarios)):
    mostrar_funcionario(
        funcionarios[numero],
        salarios[numero],
        setores[numero]
    )


print()


# Exercício 3 — Acompanhamento de projetos

projetos = [
    "Tap to Phone",
    "SmartPOS",
    "Pix no POS",
    "Link de Pagamento"
]

responsaveis = ["Ana", "Carlos", "Marina", "João"]
percentuais = [80, 100, 45, 60]


def acompanhamento_demanda(atividade, funcionario, andamento):
    print("Projeto:", atividade)
    print("Responsável:", funcionario)
    print("Conclusão:", andamento, "%")
    print("--------------------")


for numero in range(len(projetos)):
    acompanhamento_demanda(
        projetos[numero],
        responsaveis[numero],
        percentuais[numero]
    )