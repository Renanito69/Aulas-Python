w = int(input('quanto KM tem sua viagem? '))
s = w * 0.50
a = w * 0.45

if w <= 200:
    print('a sua viagem ficara no valor {}'.format(s))
else:
    print('por ser mais longa sua viagem ficara no valor {:.2f}'.format(a))

# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
