# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas

lista = []
pares = []
impar = []
while True:
    lista.append(int(input("Qual numero voce deseja adicionar a lista?: ")))
    cont = str(input("Deseja continuar? [S/N]: ")).upper()
    while cont != 'S' and cont != 'N':
        print("essa opçao nao existe...")
        cont = str(input("Deseja continuar? [S/N]: ")).upper()
    if cont == 'N':
        print("Saindo da lista...")
        break
for i, numero in enumerate(lista):
    if numero % 2 == 0:
        pares.append(numero)
    elif numero % 2 == 1:
        impar.append(numero)

print('-=' * 30)
print(f"Sua lista foi {lista}")
print(f"Sua lista so com os numeros pares {pares}")
print(f"Sua lista so com numeros impares {impar}")
