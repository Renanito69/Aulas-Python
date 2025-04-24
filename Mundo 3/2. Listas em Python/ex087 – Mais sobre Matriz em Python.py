'''Aprimore o desafio anterior, mostrando no final:   
A) A soma de todos os valores pares digitados.         
B) A soma dos valores da terceira coluna.                         
C) O maior valor da segunda linha.'''

num = [[0, 0, 0], [0, 0, 0,], [0, 0, 0]]
par = soma = maior = menor = 0

for linha in range(3):
    for coluna in range(3):
        num[linha][coluna] = int(
            input(f"Coloque um numero na posição [{linha}, {coluna}]: "))

        # Soma do numeros pares
        if num[linha][coluna] % 2 == 0:
            par += num[linha][coluna]

        # Soma dos numeros da 3 coluna
        if num[linha][coluna] == num[linha][3]:
            soma += num[linha][2]

print("-=" * 30)
for linha in range(3):
    for coluna in range(3):
        print(f"[{num[linha][coluna]:^5}]", end='')
    print()


for contagem in range(3):
    if contagem == 0:
        maior = menor = num[contagem][1]
    else:
        if num[contagem][1] > maior:
            maior = num[contagem][1]
        if num[contagem][1] < menor:
            menor = num[contagem][1]

print(f"A - As soma dos numeros pares {par}")
print(f"B - A soma dos valores na 3 coluna {soma}")
print(f"C - O maior numero na 2 coluna e {maior}")
print(f"D - O menor numero na 2 coluna e {menor}")
