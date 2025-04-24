# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}

topList = list()
print("Valores Sorteados:")
for k, v in jogo.items():
    print(f"    O {k} tirou o numero {v}")
    sleep(1)


topList = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print("-=" * 30)
print(" == RANKING DOS JOGADORES ==")
for k, v in enumerate(topList):
    print(f"    {k+1}o Lugar: {v[0]} com {v[1]} pontos")
    sleep(1)
