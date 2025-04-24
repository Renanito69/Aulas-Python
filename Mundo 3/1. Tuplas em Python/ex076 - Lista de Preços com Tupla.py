# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('arroz', 8.00,
         'lapiz', 2.50,
         'feijao', 5.99,
         'macarrao', 4.85,
         'caderno', 10.00)

# Oque eu Fiz
# i, f = 0, 1

# tamanho = len(lista)

# while f < tamanho:
#     print(f'{lista[i]}............R$ {lista[f]}')
#     i += 2
#     f += 2

# Corrigido
print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)
