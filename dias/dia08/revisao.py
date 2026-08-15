# Dia 08 - Revisão de Python

# ========================================
# 1. VARIÁVEIS E TIPOS DE DADOS
# ========================================

nome = "Raphael"
idade = 34

print(nome)
print(idade)


# ========================================
# 2. LISTAS E ÍNDICES
# ========================================

produtos = [
    "Débito",
    "Crédito",
    "Pix"
]

print(produtos[0])
print(produtos[1])
print(produtos[2])


# ========================================
# 3. LEN()
# ========================================

print(len(produtos))


# ========================================
# 4. FOR PERCORRENDO UMA LISTA
# ========================================

for produto in produtos:
    print(produto)


# ========================================
# 5. RANGE() E ÍNDICES
# ========================================

for numero in range(len(produtos)):
    print(numero)
    print(produtos[numero])


# ========================================
# 6. FUNÇÃO SIMPLES
# ========================================

def saudacao():
    print("Olá!")
    print("Bem-vindo ao sistema.")

saudacao()


# ========================================
# 7. FUNÇÃO COM PARÂMETRO
# ========================================

def mostrar_produto(nome):
    print("Produto:", nome)

mostrar_produto("SmartPOS")


# ========================================
# 8. LISTA + FOR + FUNÇÃO
# ========================================

for produto in produtos:
    mostrar_produto(produto)


# ========================================
# 9. EXERCÍCIO DA AULA
# ========================================

def projetos_andamento(projeto, status_pendente):
    print("Nome do Projeto:", projeto)
    print("Status:", status_pendente)
    print()

projetos = [
    "Tap to Phone",
    "Acordo de Incentivo",
    "Nova Política"
]

status_pendente = [
    "Sim",
    "Não",
    "Sim"
]

for numero in range(len(projetos)):
    projetos_andamento(
        projetos[numero],
        status_pendente[numero]
    )