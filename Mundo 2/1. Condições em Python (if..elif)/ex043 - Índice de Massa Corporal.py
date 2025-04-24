peso = float(input('Qual e o seu peso: '.title()).replace(',', '.'))
altura = float(input('Qual e a Sua Altura: '.title()).replace(',', '.'))
imc = (peso / altura) / altura
#imc = peso / altura ** 2

print(f'seu IMC e {imc:.2f}'.title())
if imc <= 18.5:  # Magro
    print(f'{imc:.2f} significa que voce esta abaixo do peso'.title())
elif imc <= 24.9:  # Normal
    print(f'{imc:.2f} significa que voce esta no peso ideal'.title())
    print('Parabens')
elif imc <= 29.9:  # Sobrepeso
    print(f'{imc:.2f} significa que voce esta com sobrepeso'.title())
elif imc <= 39.9:  # Obesidade
    print(f'{imc:.2f} significa que voce esta com obesidade'.title())
else:  # Obesidade Mobida
    print(f'{imc:.2f} significa que voce esta com obesidade morbida'.title())
    print('Procure Um Hospital!')

'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso


– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''
