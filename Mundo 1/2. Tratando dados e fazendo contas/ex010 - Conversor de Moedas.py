# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n = float(input('quanto dinheiros voce tem? R$ '))
s = n / 4.95

print('aqui esta quantos dolares voce pode comprar: $ {:.2f}'.format(s))