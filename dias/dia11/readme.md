# Dia 11 — Consolidação: Listas, Índices, `for` e Funções

## Objetivo da aula

A aula de hoje foi dedicada à consolidação dos conteúdos estudados anteriormente, sem introdução de um novo conceito.

O foco principal foi compreender e praticar o caminho:

**lista → índice → valor → argumento → parâmetro → execução da função**

Também foram reforçados:

- listas paralelas;
- indexação;
- `len()`;
- `range()`;
- laço `for`;
- funções;
- parâmetros e argumentos;
- uso de valores de diferentes listas em uma mesma função.

---

## 1. Revisão de `len()`, `range()` e índices

Exemplo:

```python
produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento"]
vendas = [180, 250, 140]

for indice in range(len(produtos)):
    print(produtos[indice], vendas[indice])
```

### Entendendo a estrutura

```python
len(produtos)
```

Retorna:

```text
3
```

Então:

```python
range(len(produtos))
```

equivale a:

```python
range(3)
```

O `for` trabalha, portanto, com os índices:

```text
0
1
2
```

Em cada volta, o mesmo índice pode ser utilizado para acessar valores correspondentes em diferentes listas.

Na segunda volta:

```python
indice = 1

produtos[indice]  # "Tap to Phone"
vendas[indice]    # 250
```

---

## 2. Índice não é o valor enviado à função

Este foi um dos principais pontos reforçados na aula.

Considere:

```python
produtos = ["SmartPOS", "Tap to Phone", "Link de Pagamento"]
vendas = [230, 180, 320]
metas = [200, 200, 300]

def analisar(produto, venda, meta):
    print("Produto:", produto)
    print("Vendas:", venda)
    print("Meta:", meta)

for indice in range(len(produtos)):
    analisar(produtos[indice], vendas[indice], metas[indice])
```

Na segunda volta:

```python
indice = 1
```

O índice é utilizado para localizar:

```python
produtos[1]  # "Tap to Phone"
vendas[1]    # 180
metas[1]     # 200
```

Assim, a chamada:

```python
analisar(produtos[indice], vendas[indice], metas[indice])
```

equivale, nessa execução, a:

```python
analisar("Tap to Phone", 180, 200)
```

Os parâmetros recebem:

```text
produto → "Tap to Phone"
venda   → 180
meta    → 200
```

Portanto:

> O índice não é enviado diretamente para os parâmetros. O índice é utilizado para localizar os valores nas listas, e esses valores são enviados como argumentos para a função.

---

## 3. Listas e parâmetros

É importante distinguir uma lista completa do parâmetro que recebe apenas um de seus valores.

Exemplo:

```python
conclusoes = ["75%", "90%", "60%"]
```

`conclusoes` contém todos os percentuais.

Já:

```python
def mostrar_projeto(projeto, conclusao):
```

`conclusao` recebe apenas o percentual correspondente à execução atual da função.

Por exemplo:

```python
mostrar_projeto("Dashboard Executivo", "75%")
```

Nesse momento:

```text
projeto   → "Dashboard Executivo"
conclusao → "75%"
```

---

## 4. Estrutura consolidada

Ao final da aula, foi trabalhada a seguinte estrutura:

```python
projetos = ["Dashboard Executivo", "Tap to Phone", "Automação de Relatórios"]
responsaveis = ["Ana", "Carlos", "Marina"]
conclusoes = ["75%", "90%", "60%"]

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
```

O mesmo índice mantém a correspondência entre os elementos das três listas:

```text
índice 0 → Dashboard Executivo → Ana    → 75%
índice 1 → Tap to Phone         → Carlos → 90%
índice 2 → Automação de Relatórios → Marina → 60%
```

---

## Aprendizados principais

Ao final da aula, foram consolidados os seguintes conceitos:

1. `len()` informa a quantidade de elementos de uma lista.
2. `range()` pode criar uma sequência de números utilizada pelo `for`.
3. O `for` pode percorrer índices.
4. O índice permite acessar posições correspondentes em listas paralelas.
5. O índice não é necessariamente o valor enviado para uma função.
6. `lista[indice]` retorna o valor armazenado naquela posição.
7. Esses valores podem ser enviados como argumentos.
8. Os parâmetros da função recebem os argumentos correspondentes.
9. Uma função pode receber valores de várias listas ao mesmo tempo.
10. Nomes de variáveis precisam ser utilizados de forma consistente durante todo o programa.

---

## Status da aprendizagem

O conteúdo de funções combinado com listas, índices, `for`, `range()` e `len()` apresentou evolução durante a aula.

No início, ainda houve confusão entre:

```text
índice
```

e:

```text
valor recebido pelo parâmetro
```

Ao final, foi possível construir de forma independente uma estrutura contendo:

```text
3 listas
    ↓
len()
    ↓
range()
    ↓
for
    ↓
índice
    ↓
valores correspondentes das listas
    ↓
argumentos
    ↓
parâmetros
    ↓
execução da função
```

Os erros finais estiveram relacionados principalmente à consistência dos nomes das variáveis, e não à estrutura lógica do programa.

Na próxima aula, será realizado um breve aquecimento para verificar a retenção deste conteúdo antes de avançar.