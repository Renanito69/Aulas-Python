w = float(input('qual o valor do 1 lado? '))
w2 = float(input('qual o valor do 2 lado? '))
w3 = float(input('qual o valor do 3 lado? '))

if w < w2 + w3 and w2 < w + w3 and w3 < w + w2:
    print('PODE formar um TRIANGULO')
else:
    print('NAO pode formar um TRIANGULO')

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
