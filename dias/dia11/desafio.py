# Dia 11 — Desafio Final
# Projetos, responsáveis e percentuais de conclusão


projetos = [
    "Dashboard Executivo",
    "Tap to Phone",
    "Automação de Relatórios"
]

responsaveis = [
    "Ana",
    "Carlos",
    "Marina"
]

conclusoes = [
    "75%",
    "90%",
    "60%"
]


def conclusao_projetos(projeto, responsavel, conclusao):
    print("Projeto:", projeto)
    print("Responsável:", responsavel)
    print("Conclusão:", conclusao)


for indice in range(len(projetos)):
    conclusao_projetos(
        projetos[indice],
        responsaveis[indice],
        conclusoes[indice]
    )