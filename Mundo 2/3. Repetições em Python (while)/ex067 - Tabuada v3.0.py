while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if num < 0:
        print('Programa encerrado')
        break
    for num2 in range(0, 11):
        x = num * num2
        print(f'{num} X {num2} = {x}')
    print('-' * 30)

# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
