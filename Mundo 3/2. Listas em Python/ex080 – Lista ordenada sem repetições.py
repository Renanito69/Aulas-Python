# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for contagem in range(0, 5):
    numero = int(input('Digite um valor: '))
    if contagem == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
