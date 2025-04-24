# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogos = dict()
gols = list()
jogadores = list()
sair = 0
while True:
    total = 0
    jogos['nome'] = str(input("Qual o nome do jogador: "))
    partidas = int(input(f"Quantas partidas {jogos['nome']} jogou: "))
    for p in range(partidas):
        gols.append(
            int(input(f"Quantos gols {jogos['nome']} fez na {p+1} partida: ")))
        total += gols[p]
        jogos['gols'] = gols[:]
        jogos['total'] = total
    gols.clear()
    jogadores.append(jogos.copy())

    sair = str(input("Quer contnuar: [S/N] ")).upper()
    while sair != 'S' and sair != 'N':
        print("Essa opção não existe")
        sair = str(input("Quer contnuar: [S/N] ")).upper()
    if sair == 'N':
        break

print('-=' * 15)
print('Cod ', end='')
for titulo in jogos.keys():
    print(f"{titulo:<15}", end='')
print()
print('-' * 40)
for c, j in enumerate(jogadores):
    print(f"{c:>3} ", end='')
    for dados in j.values():
        print(f"{str(dados):<15}", end='')
    print()

while True:
    sair = int(input("Mostrar dados de qual jogador: [999 para sair] "))

    if sair == 999:
        
        print("Saindo")
        break

    if sair <= len(jogadores) - 1:
        print(f" - LEVANTAMENTO DO JOGADOR: {jogadores[sair]['nome']}")
        for p, g in enumerate(jogadores[sair]['gols']):
            print(f" -- Na {p+1} partida fez {g} gols.")

    else:
        print("Esse jogador não foi cadastrado!")
