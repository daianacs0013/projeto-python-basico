"""
==========================================================================================
# EXERCÍCIO: Liquidação VoltaMax
==========================================================================================

A loja de eletrônicos VoltaMax está promovendo uma liquidação com 10% de desconto em todos 
os produtos. O sistema de ponto de venda precisa gerar automaticamente a tabela de preços 
promocionais com etiquetas numeradas e, ao final, apresentar um resumo da operação 
indicando o produto mais barato, o produto mais caro e o total economizado em toda a tabela.

Tarefa:
Desenvolva um programa que gere a lista de etiquetas promocionais a partir de uma lista de 
preços originais, obrigatoriamente utilizando list comprehension e enumerate. Ao final, 
exiba o resumo com o produto mais barato, o mais caro (pelos preços originais) e o total 
economizado com o desconto de 10%.

Entrada:
A entrada consiste em duas linhas: a primeira com os nomes dos produtos separados por vírgula 
e a segunda com os respectivos preços separados por vírgula, na mesma ordem.

Exemplo de entrada:
Notebook,Mouse,Teclado,Monitor,Headset
3200.0,89.9,150.0,1100.0,250.0

==========================================================================================
"""

# SEU CÓDIGO PYTHON:

nome_produto = input("Digite o nome dos produtos")
nome = nome_produto.split(',')

precos = input("Digite os preços dos produtos")
valor_precos = precos.split(',')

valor = [float(preco) for preco in valor_precos]
preco_desconto = [preco * 0.9 for preco in valor]

texto = "Item {item:02d}: {n} | Original: R$ {valor_orig:.2f} -> Promocional: R$ {valor_desc:.2f}"
etiquetas = [texto.format(item=i+1, n=n, valor_orig=valor[i], valor_desc=preco_desconto[i]) for i, n in enumerate(nome)]

preco_barato = min(valor)
preco_caro = max(valor)

indice_barato = valor.index(preco_barato)
indice_caro = valor.index(preco_caro)

total_economizado = sum(valor) * 0.1

for etiqueta in etiquetas:
    print(etiqueta)

print("--- Resumo ---")
print(f"Mais barato: {nome[indice_barato]} (R$ {preco_barato:.2f})")
print(f"Mais caro: {nome[indice_caro]} (R$ {preco_caro:.2f})")
print(f"Total economizado: R$ {total_economizado:.2f}")
