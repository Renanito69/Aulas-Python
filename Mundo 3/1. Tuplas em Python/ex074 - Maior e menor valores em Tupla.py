# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

lista = (random.randint(1, 10), random.randint(1, 10),
         random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

maior = max(lista)
menor = min(lista)

print(f'Os Numeros escolhidos foi', end=' ')
for numero in lista:
    print(numero, end=' ')
print(f'\nO maior numero e {maior}')
print(f'O menor numero e {menor}')
