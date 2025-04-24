'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatroze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha = int(input('Escolha um numero de 0 a 20 [-1 para sair]: '))
    if escolha == -1:
        print('saindo...')
        break
    while escolha > 20 or escolha < 0:
        print('Desculpe mais essa opçao n existe')
        escolha = int(input('Escolha um numero de 0 a 20 [-1 para sair]: '))
        if escolha == -1:
            print('saindo...')
            break
    if escolha == -1:
        break
    print(extenso[escolha])
