'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

palavra = str(input('Digite a palavra: ')).lower().replace(
    ' ', '').replace('.', '').replace(',', '')
palavra2 = palavra[::-1]

print('O inverso de {} e {}'.format(palavra, palavra2))
if palavra == palavra2:
    print('e palíndromo')
else:
    print('Nao e palíndromos')
