# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randrange
cor_amar = '\033[33m'
cor_verd = '\033[32m'
sem_cor = '\033[m'
jogador = 0
tentativas = 0
computador = randrange(10)
while jogador != computador:
    jogador = int(input('Qual e o Numero Que Estou Pensando [0 A 10]? '))
    if jogador < computador:
        print(f'{cor_amar}Mais{sem_cor}... Tente mais uma vez')
    if jogador > computador:
        print(f'{cor_amar}Menos{sem_cor}... Tente mais uma vez')
    tentativas += 1

print('Parabens Voce Acertou')
print(
    f'Foi Nescessario {cor_amar}{tentativas}{sem_cor} tentativas para acertar')
print(f'O Numero que estava pensando era {cor_verd}{computador}{sem_cor}')
