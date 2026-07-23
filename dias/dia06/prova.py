"""
Prova 1 — Fundamentos de Python

Conteúdos avaliados:
- Variáveis
- Tipos de dados
- Condicionais
- Listas
- Índices
- len()
- for
- range()
"""

# Questão 1
nome = "Raphael"
idade = 34

print(nome)
print(idade)


# Questão 2
temperatura = 18

if temperatura > 25:
    print("Quente")
else:
    print("Frio")


# Questão 3
nomes = ["Raphael", "Lucas", "Ana"]

print(nomes[1])
print(len(nomes))


# Questão 4
for numero in range(4):
    print(numero)


# Questão 5
cooperativa = "Planalto Central"
faturamento = 25000

if faturamento >= 20000:
    print(cooperativa)
    print("Meta atingida!")
else:
    print("Meta não atingida.")


# Questão 6
nomes = ["Raphael", "Lucas", "Ana"]

for indice in range(len(nomes)):
    print(indice, "-", nomes[indice])