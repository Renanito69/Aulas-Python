import math

n = float(input('qual eo valor do cateto adjesente? '))
n2 = float(input('qual eo valor do catedo oposto? '))
'''c = n ** 2
c2 = n2 ** 2
s = c + c2
r = math.sqrt(s)

print('H = C² + c²')
print('H = {}² + {}²'.format(n, n2))
print('H = {} + {}'.format(c ,c2))
print('H = √{}'.format(s))
print('H = {:.2f}'.format(r))'''
h = math.hypot(n, n2)
print('o valor da hipotenusa e {:.2f}'.format(h))

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
