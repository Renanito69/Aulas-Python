nome_velho = 0  # Pega o nome do Homen mais velho
idade_velho = 0  # Pega a idade do Homen mais velho
idade_20 = 0  # Ver quantas mulheres abaixo de 20 tem
idade_media = 0  # Soma todas as idades
for i in range(1, 5):
    print('------- {} PESSOA -------'.format(i))
    nome = str(input('Nome?  '))
    idade = int(input('Idade? '))
    idade_media += idade
    sexo = str(input('Sexo [M/F]: '))
    if sexo in 'Ff':
        if idade < 20:
            idade_20 += 1
    if sexo in 'Mm':
        if idade > idade_velho:
            idade_velho = idade
            nome_velho = nome

cont = idade_media / 4  # Dividi a soma das idade por 4

print('A Media de Idade do Grupo e {} Anos'.format(cont))
print('O Homen mais Velho tem {} Anos e se Chama {}'.format(idade_velho, nome_velho))
print('Existem {} Mulheres com menos de 20 Anos'.format(idade_20))
