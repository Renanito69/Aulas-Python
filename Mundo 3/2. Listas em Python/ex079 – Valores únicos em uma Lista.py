# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = [

]

while True:
    numero = int(input("Escolhe um numero para add na lista: "))
    if numero not in lista:
        lista.append(numero)
    else:
        print("Numero duplicado!Não irei adicionar ")
    stop = str(input("Quer continuar? [S/N]: ")).upper()
    while stop != "S" and stop != "N":
        print("Essa opçao não existe... Tenta novamente")
        stop = str(input("Quer continuar? [S/N]: ")).upper()
    if stop == "N":
        print("Finalizando lista...")
        break


lista.sort()
print(f"Sua lista e {lista}")
