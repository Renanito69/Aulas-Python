# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:                                                                                    A) Quantas pessoas foram
# cadastradas.                                                                             B) Uma listagem com as pessoas mais
# pesadas.                                                                                 C) Uma listagem com as pessoas mais leves.

pessoa = []
dados = []
maior = menor = 0

while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoa) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoa.append(dados[:])
    dados.clear()
    stop = str(input("Quer continuar? [S/N]: ")).upper()
    while stop != "S" and stop != "N":
        print("Essa opçao não existe... Tenta novamente")
        stop = str(input("Quer continuar? [S/N]: ")).upper()
    if stop == "N":
        print("Finalizando lista...")
        break

print("-=" * 30)
print(f'A - Foram cadastradas {len(pessoa)} pessoas')
print(f"B - O maior peso encontrado foi {maior}Kg. Peso de ", end='')
for nome in pessoa:
    if nome[1] == maior:
        print(f"{nome[0]}...", end='')
print('')
print(f"C - O menor peso encontrado foi {menor}Kg. Peso de ", end='')
for nome in pessoa:
    if nome[1] == menor:
        print(f"{nome[0]}...", end='')
