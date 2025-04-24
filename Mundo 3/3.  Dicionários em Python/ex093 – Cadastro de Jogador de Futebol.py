# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogos = dict()
gols = list()
total = 0
jogos['nome'] = str(input("Qual o nome do jogador: "))
partidas = int(input("Quantas partidas ele jogou: "))
for p in range(partidas):
    gols.append(int(input(f"Quantos gols na {p+1} partida? ")))
    total += gols[p]

jogos['gols'] = gols[:]
jogos['total'] = total  # ou jogos['total'] = sum(gols)

print('-=' * 30)
print(jogos)
print('-=' * 30)
for k, v in jogos.items():
    print(f"O campo {k} tem o valor {v}.")
print('-=' * 30)
print(f"O jogador {jogos['nome']} jogou {partidas} partidas.")
for p, g in enumerate(gols):
    print(f"    => Na partida {p+1}, fez {g} gols")
print(f"Foi um total de {jogos['total']} gols.")
