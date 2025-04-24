nome = input('ola quem e voce? ').upper()
cor = '\033[34m'
sem = '\033[m'

print('ola {}{}{} prazer me te conhecer'.format('\033[31m', nome, '\033[m'))

dia = input('dia? ')
mes = input('mes? ')
ano = input('ano? ')
print('voce nasceu no dia {}{}{} do mes {}{}{} no ano {}{}{} certo?'.format(
    cor, dia, sem, cor, mes, sem, cor, ano, sem))

numero = int(input('primeiro numero: '))
numero2 = int(input('segundo numero: '))
soma = numero + numero2
print('a soma dos seguintes numeros {}{}{} + {}{}{} = {}{}{}'.format('\033[33m', numero, sem, '\033[33m', numero2, sem, '\033[31m', soma, sem ))
