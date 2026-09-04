# Dia 11 — Exercícios
# Consolidação de listas, índices, for, range(), len() e funções


# ========================================
# Exercício 1 — Produtos e vendas
# ========================================

produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento"]
vendas = [180, 250, 140]

for indice in range(len(produtos)):
    print(produtos[indice], vendas[indice])


# ========================================
# Exercício 2 — Função e listas paralelas
# ========================================

produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento"]
vendas = [180, 250, 140]

def mostrar_venda(produto, quantidade):
    print("Produto:", produto)
    print("Vendas:", quantidade)

for indice in range(len(produtos)):
    mostrar_venda(produtos[indice], vendas[indice])


# ========================================
# Exercício 3 — Funcionários e salários
# ========================================

funcionarios = ["Ana", "Carlos", "Marina"]
salarios = [4500, 5200, 4800]

def mostrar_funcionario(funcionario, salario):
    print("Funcionário:", funcionario)
    print("Salário:", salario)

for indice in range(len(funcionarios)):
    mostrar_funcionario(
        funcionarios[indice],
        salarios[indice]
    )


# ========================================
# Exercício 4 — Projetos e conclusão
# ========================================

projetos = ["Dashboard", "Tap to Phone", "Automação"]
percentuais = ["80%", "60%", "90%"]

def mostrar_conclusao(projeto, percentual):
    print("Projeto:", projeto)
    print("% de Conclusão:", percentual)

for indice in range(len(projetos)):
    mostrar_conclusao(
        projetos[indice],
        percentuais[indice]
    )