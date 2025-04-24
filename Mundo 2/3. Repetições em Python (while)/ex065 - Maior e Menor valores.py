'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

sair = 'S'
quant = soma = maior = menor = 0
while sair in 'Ss':
    numero = int(input('Digite um Numero: '))
    quant += 1
    soma += numero
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
sair = str(input('Voce deseja Continuar? [S/N]: ')).upper().strip()[0]

media = soma / quant
print(f'Essa e a Soma {soma} da Quantidade de Numeros {quant}')
print(f'Essa e a Media {media}')
print(f'Esse e o Maior numero {maior}')
print(f'Esse e o Menor numero {menor}')
