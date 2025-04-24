'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

from time import sleep
total = mil = produtoBarato = valorBarato = quant = 0
while True:
    produto = str(input('Nome do Produto: '))
    valor = float(input('Preço: R$ '))
    quant += 1
    cont = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    while cont != 'S' and cont != 'N':
        cont = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]

    total += valor
    if quant == 1:
        valorBarato = valor
        produtoBarato = produto
    if valor < valorBarato:
        valorBarato = valor
        produtoBarato = produto

    if valor >= 1000:
        mil += 1
    if cont == 'N':
        print('Finalizando Compra...')
        sleep(2)
        break
print(f'Um total de {quant} Produtos')
print(f'Total gasto {total}R$')
print(f'Temos {mil} custando mais de mil')
print(
    f'O produto mais barato custava {valorBarato} e o nome dele era {produtoBarato}')
