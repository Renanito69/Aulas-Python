maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Qual e o {} Peso? '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    if peso >= maior:
        maior = peso
    if peso <= menor:
        menor = peso

print(f'O Maior peso e {maior}Kg')
print(f'O Menor peso e {menor}Kg')

# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
