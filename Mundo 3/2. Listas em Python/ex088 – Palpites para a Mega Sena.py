# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
from time import sleep

dados = list()
jogos = list()
print("-" * 30)
print(f'{"JOGAR NA MEGA SENA":^30}')
print("-" * 30)
quantidade = int(input("Quantos jogos voce deseja: "))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in dados:
            dados.append(num)
            cont += 1
            if cont >= 6:
                break
    dados.sort()
    jogos.append(dados[:])
    dados.clear()
    total += 1

print('-=' * 3, f'Sorteando {quantidade} unidade de jogos', '-=' * 3)

for cartela, numeros in enumerate(jogos):
    print(f'Jogo {cartela + 1}: {numeros}')
    sleep(1)

print(f"-=" * 5, ' <Boa Sorte> ', '-=' * 5)
