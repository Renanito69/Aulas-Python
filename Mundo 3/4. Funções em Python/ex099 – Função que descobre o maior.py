# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(* num):
    print("-=" * 20)
    print("analisando os valores passados...")
    sleep(2)
    maior = 0
    for valor in num:
        print(valor, end=' ', flush=True)
        sleep(1)
        if valor > maior:
            maior = valor
    print(f"Foram informados {len(num)} ao todo.")
    print(f"O maior valor informado foi {maior}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
