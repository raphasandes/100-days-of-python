# Dia 09 — Exercício 01
# Funções, listas e índices

funcionarios = ["Ana", "Carlos", "Marina"]
salarios = [3500, 4200, 5100]


def mostrar_funcionario(funcionario, salario):
    print("Funcionário:", funcionario)
    print("Salário:", salario)
    print()


for numero in range(len(funcionarios)):
    mostrar_funcionario(funcionarios[numero], salarios[numero])


#Esse arquivo registra o primeiro exercício que usamos para reconstruir a relação:

#lista → índice → argumento → parâmetro.