Dia 13 — Revisão dos fundamentos de Python
Data: 15/10/2026
Foco: consolidar a escrita e a interpretação de programas antes de avançar para novos conteúdos.
Objetivos
- Diferenciar lista, dicionário, índice e chave.
- Percorrer uma lista de dicionários com for.
- Acessar valores usando produto["vendas"] e produto["nome"].
- Usar if e else para classificar resultados.
- Praticar indentação, operadores de comparação, dois-pontos e parênteses.
Conceitos revisados
Conceito	Exemplo	Significado
Lista	produtos = [{...}, {...}]	Coleção ordenada de elementos.
Dicionário	{"nome": "SmartPOS", "vendas": 150}	Conjunto de pares chave–valor.
Índice	produtos[0]	Primeiro elemento da lista.
Chave	produto["vendas"]	Valor da chave "vendas" no dicionário atual.
Laço	for produto in produtos:	Percorre os elementos da lista.
Condição	if diferenca >= 0:	Executa o bloco se a condição for verdadeira.
Saída	print(produto["nome"])	Mostra o nome no terminal.


Exercícios realizados
1. Interpretação de código: cálculo de diferença entre vendas e metas e classificação dos três produtos.
2. Reforço de estruturas de dados: distinção entre índice da lista e chave do dicionário.
3. Consolidação: programa que calcula a diferença entre vendas e meta e mostra o status de cada produto.
4. Construção guiada: uso de for, if e print() para mostrar produtos com vendas acima de 120.
5. Desafio final: corrigir um programa para mostrar produtos com 200 vendas ou mais.
Os códigos executáveis corrigidos estão em exercicios.py e desafio.py.
Erros identificados e correções
Tentativa / dificuldade	Correção / aprendizado
Tratar produtos (lista) como se tivesse a chave "vendas"	Acessar a chave do dicionário atual dentro do laço: produto["vendas"].
Escrever =>	Em Python, maior ou igual é >=; estritamente maior é >.
Esquecer : após for, if ou else	Esses comandos terminam com dois-pontos.
Usar status: "Meta atingida"	Atribuição de variável usa status = "Meta atingida".
Escrever for produto in produtos(	O correto é for produto in produtos:.
Esquecer o fechamento de print()	Conferir abertura e fechamento dos parênteses.
Colocar cálculos fora do for	Manter dentro do laço as operações que devem ocorrer para cada produto.
Usar > 200 para “200 ou mais”	Usar >= 200 para incluir o valor 200.


Balanço da aula
A interpretação dos códigos e a compreensão do funcionamento do for evoluíram ao longo da revisão. A principal dificuldade observada foi escrever código de forma independente, especialmente com operadores, pontuação e organização dos blocos.
No desafio final, a sintaxe foi corrigida adequadamente; restou ajustar > 200 para >= 200 para corresponder exatamente ao enunciado.
Próxima aula — Dia 14
- Retomar listas, dicionários, for, if/else e print() sem consultar soluções.
- Construir um programa por etapas e depois de maneira independente.
- Revisar operadores e indentação.
- Somente depois de consolidar esses fundamentos, avançar para sum(), min() e max().
Decisão pedagógica: a introdução às funções de agregação foi adiada para priorizar a revisão.

Como executar
Na pasta desta aula, use:
python exercicios.py
python desafio.py
Em alguns ambientes, o comando pode ser python3.