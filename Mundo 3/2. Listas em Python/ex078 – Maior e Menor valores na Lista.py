# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = [

]

for numero in range(5):
    lista.append(int(input("Escolha um numero: ")))

maior = max(lista)
menor = min(lista)


print("=-=" * 30)
print(f"Sua lista de numeros foi {lista}")
print(
    f"O maior numero encontrado foi {maior} e esta na posição ", end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}...', end='')
print('')
print(
    f"O menor numero encontrado foi {menor} e esta na posição ", end='')

for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}...', end='')
