# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 1
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Dados Invalidos, Tenta Novamente')
    else:
        print(f'Sexo {sexo} registrado com sucesso')

print('fim')

# OU o meu /\ do professor \/

# sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
# while sexo not in 'MF':
#     sexo = str(input('Dados invalidos, Tenta novamente: ')).strip().upper()[0]
# print(f'Sexo {sexo} Confimardo com sucesso')