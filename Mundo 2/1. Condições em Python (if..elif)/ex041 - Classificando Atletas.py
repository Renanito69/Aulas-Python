from datetime import date
nasc = int(input('Em que ano voce nasceu? '.title()))
atual = date.today().year
idade = atual - nasc

print('o atleta tem {} anos'.format(idade))
if idade <= 9:  # ate 9
    print('Voce e da Categoria Mirim')
elif idade <= 14:  # dos 10 ate 14
    print('Voce e da Categoria Infantil')
elif idade <= 19:  # dos 14 ate 19
    print('Voce e da Caregoria Junior')
elif idade <= 25:  # dos 19 ate 20
    print('Voce e da Categoria Senior')
else:  # 20 pra cima
    print('Voce e da Categiria Master')

'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM


– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''
