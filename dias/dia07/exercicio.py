# Dia 07 — Funções
# Exercícios realizados durante a aula


# ==================================================
# EXERCÍCIO 1 — Primeira função
# ==================================================

def apresentacao():
    print("Meu nome é Raphael.")
    print("Estou aprendendo Python.")


apresentacao()
apresentacao()


# ==================================================
# EXERCÍCIO 2 — Ordem de execução
# ==================================================

def mensagem():
    print("Bom dia!")


print("Início")

mensagem()

print("Fim")


# ==================================================
# EXERCÍCIO 3 — Função de boas-vindas
# ==================================================

def boas_vindas():
    print("Bem-vindo ao sistema!")


print("Programa iniciado")

boas_vindas()

print("Programa encerrado")


# ==================================================
# EXERCÍCIO 4 — Ordem de definição
# ==================================================

# O código abaixo produziria um NameError porque a função seria
# chamada antes de sua definição.
#
# cumprimentar()
#
# def cumprimentar():
#     print("Olá!")

# Forma correta:

def cumprimentar():
    print("Olá!")


cumprimentar()


# ==================================================
# EXERCÍCIO 5 — Reutilização de código
# ==================================================

def linha():
    print("========================")


linha()
print("RELATÓRIO")
linha()


# ==================================================
# EXERCÍCIO 6 — Vários relatórios
# ==================================================

linha()
print("Relatório de vendas")
linha()

print()

linha()
print("Painel gerencial")
linha()

print()

linha()
print("Relatório de e-commerce")
linha()


# ==================================================
# EXERCÍCIO 7 — Desafio de previsão
# ==================================================

def mostrar_a():
    print("A")


print("1")

mostrar_a()

print("2")

mostrar_a()

print("3")