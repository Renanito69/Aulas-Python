'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:'''
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:  # ira verificar se passo e menor do que 0
        # se passo for menor do que 0 ele ira transformar o numero negativo em positivo ex(passo = -2) ira ficar (passo = 2)
        passo = -passo
        # passo *= -1 Assim tabem dá

    if passo == 0:  # verificar se o passo e igual a 0
        passo = 1  # se for verdadeiro transforma o passo(0) em passo(1)

    print('-=' * 20)
    print(f"Contagem de {inicio} ate {fim} de {passo} em {passo}")
    sleep(2.5)

    if inicio > fim:  # verificar se inicio e maior do que fim
        if passo >= 0:  # se inicio for maior do que fim, ira verificar se passo e maior do q 0
            passo = -passo  # e transforma o passo em negativo

        for x in range(inicio, fim-1, passo):
            print(x, end=' ', flush=True)
            sleep(0.5)
        print("FIM!")
        print()

    elif inicio < fim:
        for x in range(inicio, fim+1, passo):
            print(x, end=' ', flush=True)
            sleep(0.5)
        print("FIM!")
        print()


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
inicio = int(input("Qual inicia: "))
fim = int(input("Qual termina: "))
passo = int(input("Qual passa: "))

contador(inicio, fim, passo)
