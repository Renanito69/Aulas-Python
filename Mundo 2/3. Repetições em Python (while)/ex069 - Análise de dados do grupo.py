'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

from time import sleep
idade18 = 0
homens = 0
mulher20 = 0
while True:
    print('---' * 10)
    print('      CADASTRE UMA PESSOA')
    print('---' * 10)
    idade = int(input('Qual e a sua idade? '))
    sexo = str(input('Qual e o seu sexo? ')).upper().strip()[0]
    while sexo != 'M' and sexo != 'F':
        print('Erro tenta novamente')
        sexo = str(input('Qual e o seu sexo? ')).upper().strip()[0]
    sair = str(input('Voce deseja continuar[S/N]? ')).upper().strip()[0]
    if idade >= 18:
        idade18 += 1
    if sexo == 'M':
        homens += 1
    if idade < 20:
        if sexo == 'F':
            mulher20 += 1
    if sair == 'N':
        print('saindo do programa...')
        sleep(2)
        break
print(f'Existem {idade18} pessoas com mais de 18 anos')
print(f'Existem {homens} homens no grupo de pessoas')
print(f'Existem {mulher20} mulheres com menos de 20 anos')
