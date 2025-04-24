'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

dadosPessoa = dict()
pessoa = list()
sair = soma = 0

while True:
    dadosPessoa['nome'] = str(input("Nome: "))
    dadosPessoa['sexo'] = str(input("Sexo:  [M/F] ")).upper()

    while dadosPessoa['sexo'] != 'F' and dadosPessoa['sexo'] != 'M':
        print("ERRO! Por favor digite apenas M ou F")
        dadosPessoa['sexo'] = str(input("Sexo:  [M/F] ")).upper()

    dadosPessoa['idade'] = int(input("Idade: "))
    soma += dadosPessoa["idade"]
    pessoa.append(dadosPessoa.copy())
    sair = str(input("Quer Continuar: [S/N] ")).upper()

    while sair != "S" and sair != "N":
        print("ERRO! Por favor digite apens S ou N")
        sair = str(input("Quer Continuar: [S/N] ")).upper()
    if sair == "N":
        print("Saindo")
        break

media = soma / len(pessoa)

print("-=" * 30)
print(f"A - Foram cadastradas {len(pessoa)} pessoas")
print(f"B - A media de idade do grupo foi de {media:5.2f} anos")
print("C - As mulheres cadastradas foram: ", end=' ')

for mulher in pessoa:
    if mulher['sexo'] == "F":
        print(mulher['nome'], end=' ')

print()
print("D - Listas das pessoas que estão acima da media")

for maior in pessoa:
    if maior['idade'] > media:
        print()
        print(
            f"nome = {maior['nome']}; sexo = {maior['sexo']}; idade = {maior['idade']};")
        print()


print("<<<ENCERRADO>>>")

print(dadosPessoa)
