# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
print('''Qual o seu Sexo
1 - Masculino
2 - Feminino''')
sexo = int(input('Escolha uma das Opçao a Cima: '))

if sexo == 1:
    nasc = int(input('Em Que Ano Voce Nasceu? '))
    atual = date.today().year
    idade = atual - nasc

    print('Voce tem {} Anos'.format(idade))
    if idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print('Voce Ainda Ira Se Alistar')
        print('Falta {} Anos Para Voce Se Alistar'.format(saldo))
        print('Voce ira se Alistar no ano {}'.format(ano))
    elif idade == 18:
        print('Voce ira se alistar esse ano'.title())
    else:
        saldo = idade - 18
        ano = atual - saldo
        print('Ja passou da hora de se alistar'.title())
        print('Passaram {} Anos do seu alistamento'.format(saldo).title())
        print('Voce Se alistou no ano {}'.format(ano))
else:
    print('O Sexo Feminino Nao Precisa Fazer O Alistamento Obrigatorio')
    if sexo == 2:
        print('''Deseja Continuar? 
1 - Sim
2 - Nao''')
        Opçao = int(input('Escolha uma das Opçao a cima: '))
        if Opçao == 1:
            nasc = int(input('Em que ano voce nasceu? '))
            atual = date.today().year
            idade = atual - nasc

            print('Voce tem {} Anos'.format(idade))
            if idade < 18:
                saldo = 18 - idade
                ano = saldo + atual
                print('Voce ainda ira se alistar')
                print('Falta {} Anos para se Alistar'.format(saldo))
                print('Voce ira se alistar em {}'.format(ano))
            elif idade > 18:
                saldo = idade - 18
                ano = atual - saldo
                print('Ja passou da hora de se alistar!')
                print('Passaram {} Anos do seu alistamento!'.format(saldo))
                print('Voce se alistou em {}!'.format(ano))
            else:
                print('O seu Alistamento sera esse ano!')
        else:
            print('Ok OBrigado, Tenha um Bom Dia!')
