# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numero = [[], []]

for num in range(7):
    valor = int(input(f"Digite o {num+1} numero: "))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)

numero[0].sort()
numero[1].sort()

print('-=' * 30)
print(f"Os valores pares digitados foram: {numero[0]}")
print(f"Os valores impares digistado foram: {numero[1]}")
