# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('o valor: '))
s = n * 2
m = n * 3
p = n ** (1/2)

print('o dobro: {} o triplo: {} ea raiz quadrada: {:.2f}'.format(s, m, p))