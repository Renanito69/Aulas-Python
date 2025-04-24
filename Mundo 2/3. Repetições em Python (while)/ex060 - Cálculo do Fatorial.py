'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

numero = int(input('Qual e o Numero Que Deseja saber o FATORIAL? '))
numero2 = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')
while numero > 0:
    print(numero, end='')
    print(' x ' if numero > 1 else ' = ', end='')
    fatorial *= numero
    numero -= 1
print(fatorial)
print(f'O FATORIAL de {numero2}! e {fatorial}')
