"""
Dia 02 — Estruturas condicionais

Conteúdos:
- if
- elif
- else
- Operadores de comparação
- Indentação
- Diferença entre = e ==
"""

# Exercício 1 — Temperatura

temperatura = 31

if temperatura > 25:
    print("Quente")
else:
    print("Frio")


# Exercício 2 — Frete grátis

valor_compra = 250

if valor_compra >= 200:
    print("Frete grátis")
else:
    print("Frete não gratuito")


# Exercício 3 — Maioridade

idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


# Exercício 4 — Classificação por temperatura

temperatura = 20

if temperatura > 25:
    print("Quente")
elif temperatura >= 15:
    print("Agradável")
else:
    print("Frio")