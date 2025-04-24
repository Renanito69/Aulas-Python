# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('''Escolha Em Que base Quer Que ele seja Convertido:
1 - Binario
2 - Octal
3 - Hexadecimal
4 - Converter Para Decimal''')

opçao = int(input('Opçao: '))
if opçao == 1 or opçao == 2 or opçao == 3:
    valor = int(input('Coloque um Valor: '))

    if opçao == 1:
        print('Na Opçao de Binario o Valor {} sera {}'.format(
            valor, bin(valor)[2:]))
    elif opçao == 2:
        print('Na Opçao de Octal o Valor {} sera {}'.format(
            valor, oct(valor)[2:]))
    elif opçao == 3:
        print('Na Opçao de Hexadecimal o Valor {} sera {}'.format(
            valor, hex(valor)[2:]))
if opçao == 4:
    print('''Escolha Em Que base Quer Que ele seja Desconvertido
5 - Binario para Decimal
6 - Octal para Decimal
7 - Hexadecimal para Decimal''')
    opçao2 = int(input('Opçao: '))
    if opçao2 == 1:
        print('Essa Opçao Nao Esta Pronta!')

    elif opçao2 == 2:
        print('Essa Opçao Nao Esta Pronta!')
    elif opçao2 == 3:
        print('Essa Opçao Nao Esta Pronta!')
    else:
        print('Essa Opçao Nao Existe!')

else:
    print('Essa Opçao Não Existe!')
