"""
Dia 04 — Revisão dos fundamentos

Conteúdos revisados:
- Variáveis
- Tipos de dados
- Condicionais
- Listas
- Índices
- len()
- Indentação
"""

nome = "Raphael"
idade = 34
estuda_python = True

print(nome)
print(idade)
print(estuda_python)


temperatura = 18

if temperatura > 25:
    print("Quente")
else:
    print("Frio")


nomes = ["Raphael", "Lucas", "Ana"]

print(nomes[0])
print(nomes[1])
print(nomes[2])
print(len(nomes))


faturamento = 25000

if faturamento >= 20000:
    print("Meta atingida!")
else:
    print("Meta não atingida.")