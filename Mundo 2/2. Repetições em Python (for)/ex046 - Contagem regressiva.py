# baixar a biblioteca emoji com: pip install emoji

from time import sleep
from emoji import *

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('{:=^40}'.format(' OS FOGOS EXPLODIUUU '))
print(emojize(':colisão:', language='pt'))

# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
