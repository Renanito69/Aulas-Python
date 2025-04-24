# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

atual = datetime.date.today().year
idade_21 = 0
idade_20 = 0
for inicio in range(1, 8):
    ano = int(input('Em que ano a {} pessoa nasceu? '.format(inicio)))
    cont = atual - ano
    if cont > 21:
        idade_21 += 1
    else:
        idade_20 += 1
print('existem {} pessoas Maior de Idade'.format(idade_21))
print('e existem {} pessoas Menor de Idade'.format(idade_20))
