l1 = float(input('Qual eo valor do 1 lado do triangulo? '.title()))
l2 = float(input('Qual eo valor do 2 lado do triangulo? '.title()))
l3 = float(input('Qual eo valor do 3 lado do triangulo? '.title()))

if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
    print('Nao e um Triangulo!')
elif l1 == l2 and l1 == l3:
    print('E um Triangulo Equilatero')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('E um Triangulo Isoceles')
else:
    print('E um Triangulo Escaleno')

'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais


– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

Aula Anterior
'''
