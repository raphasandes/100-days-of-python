# Desafio — Dia 07

Crie um programa chamado `sistema_relatorios.py`.

O programa deverá utilizar funções para apresentar três relatórios fictícios:

1. Relatório de clientes;
2. Relatório de pedidos;
3. Relatório de entregas.

## Requisitos

Crie uma função chamada:

```python
linha()
```

Ela deve imprimir uma linha de separação.

Crie também uma função:

```python
titulo(texto)
```

Ela deve utilizar `linha()` para produzir um cabeçalho.

Exemplo:

```text
========================================
RELATÓRIO DE CLIENTES
========================================
```

Depois, crie as funções:

```python
relatorio_clientes()
relatorio_pedidos()
relatorio_entregas()
```

Cada função deve apresentar pelo menos dois dados fictícios.

## Regras

- Utilize dados totalmente fictícios;
- Não utilize nomes de empresas ou produtos reais;
- Evite repetir diretamente a linha de separação;
- Utilize nomes claros para as funções;
- Chame os três relatórios no programa principal.

## Pergunta de reflexão

Se fosse necessário alterar o tamanho da linha de separação em todos os relatórios, quantas linhas do código precisariam ser modificadas?

Explique por quê.