# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

import random
from time import sleep


numeros = list()

def sorteia():
    print(f"Sorteando os valores ", end='')
    for x in range(5):
        numeros.append(random.randint(0, 10))
        print(numeros[x], end=' ', flush=True)
        sleep(1)
    print("PRONTO!")

def somaPar(lista):
    num = 0
    for valor in lista:
        if valor % 2 == 0:
            num += valor
    print(f"Somando os numeros pares de {lista} temos {num}")


sorteia()
somaPar(lista=numeros)
