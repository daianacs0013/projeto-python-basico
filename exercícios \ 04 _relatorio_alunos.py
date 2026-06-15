"""
==========================================================================================
EXERCÍCIO 4: Relatórios de Desempenho da Faculdade Horizonte
==========================================================================================

A secretaria da Faculdade Horizonte precisa gerar dois relatórios automaticamente após o 
lançamento das notas: o primeiro lista os alunos aprovados com suas respectivas notas, 
e o segundo classifica cada aluno com um conceito de desempenho:
- Ótimo para nota maior ou igual a 8.0
- Bom para nota maior ou igual a 6.0 e menor que 8.0
- Insuficiente para nota menor que 6.0

Tarefa:
Desenvolva um programa que produza dois relatórios a partir de uma lista de registros de 
alunos, obrigatoriamente utilizando list comprehension com condicional em ambos os casos:
1. Lista de aprovados, contendo apenas alunos com nota maior ou igual a 6.0, exibindo nome e nota.
2. Lista de todos os alunos com nome e conceito de desempenho.

Entrada:
A entrada será uma lista chamada 'alunos' em que cada elemento também é uma lista contendo 
o nome do aluno e sua nota.

==========================================================================================
"""

# SEU CÓDIGO PYTHON COMEÇA AQUI:

alunos = [
    ["Ana", 8.5],
    ["Bruno", 4.0],
    ["Carla", 6.0],
    ["Diego", 3.5],
    ["Elisa", 7.2],
    ["Fátima", 9.1]
]

# Relatório 1: Lista de aprovados (nota maior ou igual a 6.0)
aprovados = [f"{aluno[0]} - {aluno[1]}" for aluno in alunos if aluno[1] >= 6.0]

print("--- Relatório 1: Alunos Aprovados ---")
for item in aprovados:
    print(item)

print() # Linha em branco para separar um relatório do outro

# Relatório 2: Lista com conceitos de desempenho de todos os alunos
conceitos = [
    f"{aluno[0]} - {'Ótimo' if aluno[1] >= 8.0 else 'Bom' if aluno[1] >= 6.0 else 'Insuficiente'}"
    for aluno in alunos
]

print("--- Relatório 2: Conceito de Desempenho ---")
for item in conceitos:
    print(item)
