# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

aluno = []
dados = []
sair = 0
while True:
    dados.append(str(input("Nome: ")))  # Nome
    dados.append(float(input("Nota 1: ")))  # Nota 1
    dados.append(float(input("Nota 2: ")))  # Nota 2
    soma = dados[1] + dados[2]
    media = soma / 2
    dados.append(media)  # dados.append([Nome, [Nota1, Nota2], media])
    aluno.append(dados[:])
    dados.clear()
    stop = str(input("Quer continuar? [S/N]: ")).upper()
    while stop != "S" and stop != "N":
        print("Essa opçao não existe... Tenta novamente")
        stop = str(input("Quer continuar? [S/N]: ")).upper()
    if stop == "N":
        print("Finalizando lista...")
        break

print("-=" * 30)
print(f'{"BOLETIM":^60}')
print("-=" * 30)
print(f"{'No.':<4}{'NOME':<10}{'MEDIA':>8}")
for i, a, in enumerate(aluno):
    print(f"{i:<4}{a[0]:<10}{a[3]:>8.1f} ")
while True:
    sair = int(input("Mostrar nota de qual aluno? (999 para interromper): "))

    if sair == 999:
        print("Finalizando")
        break
    if sair <= len(aluno) - 1:
        print(
            f"As notas de {aluno[sair][0]} são {aluno[sair][1]} e {aluno[sair][2]}")
    else:
        print("Esse aluno não existe")

print("<<< Volte Sempre >>>")
