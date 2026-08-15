# Dia 09 — Exercício 02
# Funções, listas, índices, len() e range()

produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento"]
precos = [150, 100, 80]


def mostrar_produto(produto, preco):
    print("Produto:", produto)
    print("Preço:", preco)
    print()


for indice in range(len(produtos)):
    mostrar_produto(produtos[indice], precos[indice])


#Aqui registramos o momento em que você começou a construir sozinho a combinação entre for, range(), len() e a chamada da função.