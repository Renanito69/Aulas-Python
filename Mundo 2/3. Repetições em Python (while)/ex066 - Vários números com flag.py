'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

valor = 0
quant = 0
while True:
    numero = int(input('Coloque um numero [999 para sair do app]: '))
    if numero == 999:
        break
    valor += numero
    quant += 1
print(f'A soma dos {quant} valore foi {valor}')
