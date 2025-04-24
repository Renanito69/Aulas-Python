'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

sep = '=' * 40

n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
titulo = 'BANCO DO RENAN'

print(f'{sep}\n{titulo:^40}\n{sep}')
valor = int(input('Qual Valor Voce deseja sacar? '))
valor2 = valor

while valor >= 100:
    valor -= 100
    n100 += 1

while valor >= 50:
    valor -= 50
    n50 += 1

while valor >= 20:
    valor -= 20
    n20 += 1

while valor >= 10:
    valor -= 10
    n10 += 1

while valor >= 5:
    valor -= 5
    n5 += 1

while valor >= 2:
    valor -= 2
    n2 += 1

print(f'pra sacar {valor2} sao necessarios um total de')
print(f'{n100} cedulas de 100')
print(f'{n50} cedulas de 50')
print(f'{n20} cedulas de 20')
print(f'{n10} cedulas de 10')
print(f'{n5} cedulas de 5')
print(f'{n2} cedulas de 2')
