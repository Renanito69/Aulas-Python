w = float(input('Quantos Km/h estava o carro? '))
s = w - 80
a = s * 7

if w <= 80:
    print('voce esta na velocidade certa')
else:
    print('Voce esta rapido demais e levara uma multa de {} reais'.format(a))

# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
