# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

turma = dict()

turma['nome'] = str(input("Nome: "))
turma['media'] = float(input(f"Media de {turma['nome']}: "))

print('-=' * 30)
print(f" - Nome e igual a {turma['nome']}")
print(f" - Media e igual a {turma['media']}")

if turma['media'] >= 7:
    turma['situacao'] = "Aprovado"

elif turma['media'] >= 5:
    turma['situacao'] = "Recuperação"

else:
    turma['situacao'] = "Reprovado"

print(f" - Situação do aluno {turma['nome']} e {turma['situacao']}")
