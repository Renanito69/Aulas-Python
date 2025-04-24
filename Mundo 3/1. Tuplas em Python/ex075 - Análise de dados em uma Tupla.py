'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

numeros = (int(input('Digite o Primeiro numero: ')),
           int(input('Digite o Segundo numero: ')),
           int(input('Digite o Mais um numero: ')),
           int(input('Digite o Ultimo numero: ')))

num9 = numeros.count(9)
VerTres = numeros.count(3)
# par = 0
# qpar = ''
quantidadePar = 0

print(f'Os numeros digitados foram {numeros}')
if num9 == 1:
    print(f'O numero 9 apareceu {num9} vez')
elif num9 == 0:
    print('Nao foi digitado o numero 9')
else:
    print(f'O numero 9 apareceu {num9} Vezes')
if VerTres == 1:
    tres = numeros.index(3)
    print(f'O numero 3 apareceu pela primeira vez na posiçao {tres+1}')
else:
    print('Nao Tem 3 nos numeros digitados')
for num in numeros:
    if num % 2 == 0:
        print('Os Numeros PARES digitador foram', end=' ')
        break
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')


# for num in numeros:
#     if num % 2 == 0:
#         par += 1
#         qpar += ' ' + str(num)
# if par > 0:
#     print(f'O Numeros digitado par foram {qpar}')
# else:
#     print(f'Nao tem Numeros par')
