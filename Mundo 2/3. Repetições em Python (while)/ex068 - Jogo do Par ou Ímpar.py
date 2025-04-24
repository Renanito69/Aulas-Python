'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

import random
print('=-=' * 8)
print('VOMOS JOGAS PAR OU IMPAR')
print('=-=' * 8)
vitorias = 0

while True:
    computador = random.randrange(10)
    jogador = int(input('Qual numero voce quer joga? '))
    opcao = str(
        input('Voce deseja jogar impar ou par [I/P]: ')).upper().strip()[0]
    while opcao not in 'IP':
        opcao = str(
            input('Voce deseja jogar impar ou par [I/P]: ')).upper().strip()[0]
        
    total = computador + jogador
    print('=-=' * 10)
    print(f'Voce Jogou {jogador} e o computador {computador}. Total deu {total}')
    print('=-=' * 10)
    jogo = total % 2
    if opcao == 'I':
        if jogo == 1:
            print(f'O numero {total} e Impar')
            print('Voce \033[;;32mGanhou\033[m')
            vitorias += 1
        else:
            print('Voce \033[31mPerdeu\033[m')
            break
    if opcao == 'P':
        if jogo == 0:
            print(f'O numero {total} e Par')
            print('Voce \033[32mGanhou\033[m')
            vitorias += 1
        else:
            print(f'A total dos numero deu {total} e é impar')
            print('Voce \033[31mPerdeu\033[m')
            break
print(f'Voce ganhou {vitorias} vezes seguidas')
