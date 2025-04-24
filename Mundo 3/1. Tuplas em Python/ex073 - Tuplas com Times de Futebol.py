'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

times_brasileirao = (
    "Flamengo",
    "Palmeiras",
    "São Paulo",
    "Corinthians",
    "Santos",
    "Atlético Mineiro",
    "Grêmio",
    "Internacional",
    "Cruzeiro",
    "Vasco da Gama",
    "Fluminense",
    "Botafogo",
    "Atlético Paranaense",
    "Bahia",
    "Ceará",
    "Fortaleza",
    "Goiás",
    "Sport Recife",
    "Coritiba",
    "Chapecoense"
)

print('1 - Apenas os 5 primeiros colodados\n2 - Os ultimos 5 colocados\n3 - Uma lista em ordem alfabetica\n4 - Em que posiçao esta o time chapecoense')
escolha = int(input('Escolha uma opçao: '))
if escolha == 1:
    for lugar, time in enumerate(times_brasileirao[:5]):
        print(f'{lugar+1} --> {time}')
elif escolha == 2:
    for lugar, time in enumerate(times_brasileirao[-5:]):
        print(f'{lugar+16} --> {time}')
elif escolha == 3:
    for lugar, time in enumerate(sorted(times_brasileirao)):
        print(f'{lugar+1} --> {time}')
elif escolha == 4:
    chape_posi = times_brasileirao.index('Chapecoense')
    print(f'a posiçao do Chapecoense e {chape_posi+1}')