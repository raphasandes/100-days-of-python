# Dia 07 — Funções

## Objetivo da aula

Nesta aula, estudei como criar e executar funções em Python.

As funções permitem organizar o programa em blocos reutilizáveis, reduzir repetições e facilitar futuras alterações no código.

## Conteúdos estudados

- Criação de funções com `def`;
- Chamada de funções;
- Diferença entre definir e executar uma função;
- Ordem de execução do programa;
- Reutilização de código;
- Funções chamando outras funções;
- Introdução aos parâmetros;
- Organização de um programa em partes menores.

## Primeira função

```python
def saudacao():
    print("Olá!")


saudacao()
```

A palavra `def` é utilizada para definir uma função.

Criar uma função não significa executá-la. Para que seu conteúdo seja executado, é necessário chamar a função pelo nome:

```python
saudacao()
```

## Ordem de execução

O Python executa o código de cima para baixo.

```python
def mensagem():
    print("Bom dia!")


print("Início")
mensagem()
print("Fim")
```

Saída:

```text
Início
Bom dia!
Fim
```

Primeiro, a função é definida. Depois, o programa imprime `Início`, chama a função e, ao final dela, continua a execução com `Fim`.

## Reutilização de código

Uma função pode ser executada várias vezes:

```python
def linha():
    print("========================")


linha()
print("RELATÓRIO")
linha()
```

A principal vantagem não é necessariamente utilizar menos memória, mas tornar o código:

- mais organizado;
- mais legível;
- mais reutilizável;
- mais fácil de corrigir;
- mais fácil de atualizar.

Caso o formato da linha precise ser alterado, basta modificar uma única parte do programa.

## Introdução aos parâmetros

No mini-projeto, foi utilizada uma função que recebe uma informação:

```python
def titulo(texto):
    print(texto)
```

Ao chamar a função, enviamos o conteúdo:

```python
titulo("RELATÓRIO DE VENDAS")
```

O valor `"RELATÓRIO DE VENDAS"` é recebido pelo parâmetro `texto`.

Esse conteúdo será aprofundado nas próximas aulas.

## Mini-projeto

O mini-projeto da aula foi um gerador de relatórios.

O programa utiliza funções para gerar relatórios fictícios de:

- vendas;
- estoque;
- informações financeiras.

Uma função é responsável pela linha de separação:

```python
def linha():
    print("========================================")
```

Outra função gera o título completo:

```python
def titulo(texto):
    linha()
    print(texto)
    linha()
```

As funções específicas utilizam esse cabeçalho para apresentar os dados dos relatórios.

## Organização do programa

```text
Programa principal
│
├── relatorio_vendas()
│   └── titulo()
│       └── linha()
│
├── relatorio_estoque()
│   └── titulo()
│       └── linha()
│
└── relatorio_financeiro()
    └── titulo()
        └── linha()
```

## Principais aprendizados

- Definir uma função não significa executá-la.
- Uma função precisa ser definida antes de ser chamada.
- Uma função pode ser chamada várias vezes.
- Funções ajudam a evitar repetição de código.
- Uma função pode chamar outra função.
- Parâmetros permitem que a mesma função trabalhe com informações diferentes.
- Bons nomes tornam o código mais fácil de compreender.

## Observação sobre os dados

Este projeto foi desenvolvido exclusivamente para fins educacionais.

Todos os nomes, empresas, clientes, valores e cenários apresentados são fictícios ou anonimizados. Nenhuma informação interna, confidencial ou pertencente a organizações reais foi utilizada.