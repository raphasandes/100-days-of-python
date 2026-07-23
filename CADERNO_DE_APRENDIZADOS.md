# 📚 Caderno de Aprendizados

Este documento reúne os principais aprendizados construídos ao longo do projeto **100 Days of Python**.

O objetivo não é registrar apenas erros, mas transformar dúvidas, hipóteses, correções e descobertas em conhecimento permanente.

Sempre que um conceito importante surgir durante os estudos, ele será registrado aqui.

---

# Prova 1 — Fundamentos de Python

## 1. Como funciona o `range()`

### Minha hipótese inicial

Eu pensei que o número 4 não aparecia em `range(4)` apenas porque a contagem começava em zero.

### O que aprendi

O principal motivo é que:

```python
range(4)
```

gera os seguintes valores:

```text
0
1
2
3
```

O valor final funciona como um limite e **não é incluído**.

### Regra para lembrar

> `range(n)` gera valores de `0` até antes de `n`.

### Exemplo

```python
for numero in range(4):
    print(numero)
```

Saída:

```text
0
1
2
3
```

---

## 2. Como `len()` trabalha junto com `range()`

### Minha dúvida inicial

Eu pensei que a variável do `for` receberia diretamente o valor retornado por `len()`.

### O que aprendi

Considere esta lista:

```python
nomes = ["Raphael", "Lucas", "Ana"]
```

A função:

```python
len(nomes)
```

retorna:

```text
3
```

Depois:

```python
range(3)
```

gera:

```text
0
1
2
```

Por fim, a variável `indice` recebe esses valores, um por vez.

### Fluxo completo

```text
nomes = ["Raphael", "Lucas", "Ana"]
                ↓
           len(nomes)
                ↓
                3
                ↓
            range(3)
                ↓
             0, 1, 2
                ↓
             indice
```

### Exemplo

```python
nomes = ["Raphael", "Lucas", "Ana"]

for indice in range(len(nomes)):
    print(indice)
```

Saída:

```text
0
1
2
```

### Regra para lembrar

> `len()` informa a quantidade de elementos.  
> `range()` transforma essa quantidade em uma sequência de índices.

---

## 3. Lista inteira x elemento da lista

### Minha hipótese inicial

Eu imaginei que `nomes[indice]` servia para criar uma ordem lógica entre o índice e o nome.

### O que aprendi

Essa intuição estava próxima do conceito correto.

A variável:

```python
nomes
```

representa a lista inteira.

Exemplo:

```python
print(nomes)
```

Saída:

```text
['Raphael', 'Lucas', 'Ana']
```

Já:

```python
nomes[indice]
```

acessa apenas o elemento localizado na posição indicada pelo índice.

### Exemplos

```text
nomes[0] → Raphael
nomes[1] → Lucas
nomes[2] → Ana
```

### Uso dentro do `for`

```python
nomes = ["Raphael", "Lucas", "Ana"]

for indice in range(len(nomes)):
    print(indice, "-", nomes[indice])
```

Saída:

```text
0 - Raphael
1 - Lucas
2 - Ana
```

### Regra para lembrar

> O nome da lista representa todos os elementos.  
> O nome da lista com um índice acessa apenas um elemento.

---

## 4. Índices começam em zero

### O que aprendi

Em Python, o primeiro elemento de uma lista tem índice zero.

Considere:

```python
nomes = ["Raphael", "Lucas", "Ana"]
```

Os índices são:

```text
0 → Raphael
1 → Lucas
2 → Ana
```

Por isso:

```python
print(nomes[1])
```

imprime:

```text
Lucas
```

### Uma forma útil de visualizar

O índice representa a distância do elemento em relação ao início da lista:

```text
Raphael está a 0 posições do início.
Lucas está a 1 posição do início.
Ana está a 2 posições do início.
```

---

## 5. Índice inexistente

### O que aprendi

Uma lista com três elementos possui os índices:

```text
0
1
2
```

Por isso, tentar acessar:

```python
nomes[3]
```

gera um erro.

### Erro apresentado

```text
IndexError: list index out of range
```

### Regra para lembrar

> A quantidade de elementos não é igual ao último índice.

Uma lista com três elementos tem tamanho `3`, mas seu último índice é `2`.

---

## 6. Indentação define os blocos de código

### O que aprendi

Em Python, a indentação define quais comandos pertencem ao `if`, ao `else`, ao `for` e a outros blocos.

Exemplo:

```python
cooperativa = "Planalto Central"
faturamento = 25000

if faturamento >= 20000:
    print(cooperativa)
    print("Meta atingida!")
else:
    print("Meta não atingida.")
```

Os dois comandos abaixo pertencem ao bloco do `if`:

```python
print(cooperativa)
print("Meta atingida!")
```

Eles só serão executados quando a condição for verdadeira.

### Caso a condição seja falsa

Se o faturamento fosse:

```python
faturamento = 18000
```

a saída seria:

```text
Meta não atingida.
```

O nome da cooperativa não apareceria, pois o comando que o imprime está dentro do bloco do `if`.

### Regra para lembrar

> Linhas com a mesma indentação pertencem ao mesmo bloco.

---

## 7. Condição verdadeira ou falsa

### O que aprendi

O Python avalia uma condição como:

```text
True
```

ou:

```text
False
```

Exemplo:

```python
temperatura = 18

if temperatura > 25:
    print("Quente")
else:
    print("Frio")
```

A condição:

```python
18 > 25
```

é falsa.

Por isso, o Python ignora o bloco do `if` e executa o bloco do `else`.

### Ajuste importante

Não é apenas o "próximo comando" que será executado. O Python executa especificamente o bloco correspondente ao resultado da condição.

---

## 8. Tipos de dados em Python

### String

Valores de texto são normalmente escritos entre aspas:

```python
nome = "Raphael"
```

O tipo é:

```python
str
```

### Número inteiro

Valores numéricos sem casas decimais:

```python
idade = 34
```

O tipo é:

```python
int
```

### Ajuste de vocabulário

A palavra em inglês é:

```text
integer
```

Em Python, usamos a abreviação:

```python
int
```

---

# Git e GitHub

## 9. Comandos não usam hífen depois de `git`

### O que eu escrevi

```bash
git -status
git -push
```

### Forma correta

```bash
git status
git push
```

O nome do comando vem separado por espaço, sem hífen depois de `git`.

---

## 10. Fluxo básico do Git

O fluxo básico que devo utilizar ao final das aulas é:

```bash
git status
git add .
git commit -m "Mensagem do commit"
git push
```

### Significado de cada etapa

#### `git status`

Mostra o que foi alterado no repositório.

```bash
git status
```

#### `git add .`

Prepara todas as alterações para o commit.

```bash
git add .
```

O ponto significa que serão adicionadas as alterações da pasta atual.

Também é possível preparar apenas um arquivo:

```bash
git add dias/dia06-prova-01/prova.py
```

#### `git commit -m`

Registra as alterações localmente com uma mensagem.

```bash
git commit -m "Documenta Prova 1"
```

A opção `-m` indica a mensagem do commit.

#### `git push`

Envia os commits do computador para o GitHub.

```bash
git push
```

### Regra para lembrar

> Status → Add → Commit → Push

Ou:

> Olhar → Preparar → Registrar → Enviar

---

# Lições sobre o processo de aprendizagem

## 11. Acertar a saída não significa compreender completamente

Em alguns exercícios, consegui prever corretamente a saída do código, mas não expliquei com precisão o motivo.

Isso mostrou que existem dois níveis de aprendizado:

1. identificar o resultado;
2. compreender o fluxo que produziu o resultado.

Meu objetivo será desenvolver os dois.

---

## 12. Formular hipóteses faz parte do aprendizado

Mesmo quando minhas respostas não estavam totalmente corretas, algumas hipóteses estavam próximas do conceito real.

Um exemplo foi a ideia de que:

```python
nomes[indice]
```

conectava o índice ao nome.

A explicação precisava de mais precisão, mas o raciocínio apontava para a função correta dos índices.

### Aprendizado

> Uma resposta incompleta pode revelar que o raciocínio está em construção.

---

## 13. Honestidade diante da dúvida

Durante a prova, indiquei quando não tinha certeza sobre uma resposta.

Isso é importante porque permite identificar os conceitos que precisam de revisão.

### Aprendizado

> Reconhecer uma dúvida é o primeiro passo para resolvê-la.

---

## 14. Revisar antes de avançar

Os pontos de maior dificuldade da Prova 1 foram:

- funcionamento do `range()`;
- relação entre `len()` e `range()`;
- valores assumidos pela variável de um `for`;
- uso de índices para acessar elementos de uma lista;
- comandos básicos do Git.

Esses conceitos serão revisados antes do início do próximo conteúdo.

### Regra de estudo

> Não avançar apenas para terminar o conteúdo.  
> Avançar depois de compreender os fundamentos.

---

# Rotina de encerramento das aulas

A partir desta etapa, toda aula de Python deverá terminar com:

1. revisão do que foi aprendido;
2. registro da reflexão do dia;
3. atualização do Caderno de Aprendizados, quando necessário;
4. atualização do `README.md` do projeto;
5. verificação das alterações com Git;
6. commit;
7. envio para o GitHub.

### Fluxo final

```bash
git status
git add .
git commit -m "Mensagem relacionada à aula"
git push
```

---

# Histórico de aprendizados

| Data | Aula | Principais aprendizados |
|---|---|---|
| 23/07/2026 | Prova 1 | Funcionamento de `range()`, relação entre `len()` e índices, fluxo do `for`, indentação e comandos básicos do Git. |

---

# Próximas revisões

- [ ] Praticar `range(4)`.
- [ ] Praticar `range(inicio, fim)`.
- [ ] Praticar `range(inicio, fim, passo)`.
- [ ] Revisar o fluxo de execução do `for`.
- [ ] Revisar acesso a elementos com índices.
- [ ] Repetir o fluxo básico do Git sem consulta.