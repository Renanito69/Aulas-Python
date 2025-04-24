'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
print('{:=^40}'.format('Calculadora'))
num1 = int(input('Digite Primeiro Numero: '))
num2 = int(input('Digite o Segundo Numero: '))
escolha = 0
while escolha != 5:
    print('''    1 - Soma
    2 - Multiplicar
    3 - Maior
    4 - Novos Numeros
    5 - Finalizar o Programa''')
    escolha = int(input('>>>> Qual Operaçao Deseja: '))
    if escolha == 1:
        soma = num1 + num2
        print(f'A Soma Dos Numero {num1} + {num2} = {soma}')
    elif escolha == 2:
        mult = num1 * num2
        print(f'A Multiplicaçao Dos Numeros {num1} x {num2} = {mult}')
    elif escolha == 3:
        maior = max(num1, num2)
        print(f'O Maior Numero entre {num1} e {num2} é {maior}')
    elif escolha == 4:
        num1 = int(input('Digite Primeiro Numero: '))
        num2 = int(input('Digite o Segundo Numero: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opçao Invalida, Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Finalizado, Volte sempre')
