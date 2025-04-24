w = int(input('digite um numero de 0 a 9999: '))

'''print('unidade:', w[3])
print('dezena:', w[2])
print('centena:', w[1])
print('milhar:', w[0])'''

#do prof:

u = w // 1 % 10
d = w // 10 % 10
c = w // 100 % 10
m = w // 1000 % 10

print('analisando o numero {}'.format(w))
print('unidade: {}'.format(u))
print('dezena: {}' .format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
