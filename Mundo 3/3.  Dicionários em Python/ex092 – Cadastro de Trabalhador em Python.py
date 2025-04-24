# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime

pessoa = dict()
anoAtual = datetime.date.today().year

pessoa['nome'] = str(input("Nome: "))
idade = int(input("Ano de Nascimento: "))
pessoa['idade'] = anoAtual - idade
pessoa['carteira'] = int(input("Carteira de Trabalho (0 Não tem): "))
if pessoa['carteira'] != 0:  # ou tabem if pessoa['contatacao'] > 0:
    pessoa['contratacao'] = int(input("Ano de Contratação: "))
    pessoa['salario'] = float(input("Salario: "))
    pessoa['aposentadoria'] = pessoa['idade'] + \
        ((pessoa['contratacao'] + 35) - datetime.date.today().year)


print('-=' * 30)
print(pessoa)
for k, v in pessoa.items():
    print(f" - {k} tem o valor {v}")
