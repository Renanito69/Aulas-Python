# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep
Jogo = int(input(
    '''Escolha alguma Opçao
1 - Pedra
2 - Papel
3 - Tesoura
Qual e a Sua escolha: '''))

lista = ',', 'Pedra', 'Papel', 'Tesoura'
Robo = random.randint(1, 3)

if Jogo >= 4:
    print('Essa Opçao Nao Existe')
else:
    print('JOO')
    sleep(1)
    print('KEEN')
    sleep(1)
    print('POO!!!')

    print('-='*20)
    print('Voce Escolheu {}'.format(lista[Jogo]))
    print('O Robo Escolheu {}'.format(lista[Robo]))
    print('-='*20)

    if Robo == 1:
        if Jogo == 1:
            print('Impate!')
        elif Jogo == 2:
            print('Voce \033[;32mGanhou!')
        elif Jogo == 3:
            print('Voce \033[;31mPerdeu')
        else:
            print('ERRO')

    if Robo == 2:
        if Jogo == 1:
            print('Voce \033[:31mPerdeu!')
        elif Jogo == 2:
            print('Impate!')
        elif Jogo == 3:
            print('Voce \033[;32mGanhou!')
        else:
            print('ERRO')

    if Robo == 3:
        if Jogo == 1:
            print('Voce \033[;32mGanhou!')
        elif Jogo == 2:
            print('Voce \033[;31mPerdeu')
        elif Jogo == 3:
            print('Impate!')
        else:
            print('ERRO')

