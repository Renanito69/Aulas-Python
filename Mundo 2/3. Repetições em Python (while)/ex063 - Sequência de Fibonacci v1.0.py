'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''

print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
termo = int(
    input('Quantos Termos voce quer mostras da sequencia de fibonacci? '))
contador = 1
numero_1 = 1
numero_2 = 0
print('~' * 30)
print(0, end=(' --> '))
while contador != termo:
    contador += 1
    soma = numero_1 + numero_2
    numero_1 = numero_2
    numero_2 = soma
    print(soma, end=(' --> '))
print('acabou')
print('~' * 30)
