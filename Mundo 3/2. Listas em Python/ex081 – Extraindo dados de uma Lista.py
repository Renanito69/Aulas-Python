# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(
        int(input("Qual Numero deseja adicionar na sua lista?: ")))
    stop = str(input("Deseja continuar? [S/N]: ")).upper()
    while stop != 'S' and stop != 'N':
        print("Essa opçao nao existe...")
        stop = str(input("Deseja continuar? [S/N]: ")).upper()
    if stop == "N":
        print("Saindo do programa...")
        break

print('=-=' * 30)
print(f"A - Quantos Numero foi digitados: {len(lista)}")
lista.sort()
print(f"B - A lista em forma crecente {lista}")
lista.sort(reverse=True)
print(f"C - A lista em forma descrecente {lista}")
if 5 in lista:
    print(f"D - O numero 5 foi digitado {lista.count(5)} vezes")
else:
    print('D - Não tem o numero 5 na lista')
