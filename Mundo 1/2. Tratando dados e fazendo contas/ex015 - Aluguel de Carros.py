d = int(input('Quantos dias alugou o carro? '))
k = float(input('Quanto Km andou com o carro? '))
n = d * 60
n2 = k * 0.15
n3 = n + n2

print('o valor a paga e {:.2f}'.format(n3))

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
