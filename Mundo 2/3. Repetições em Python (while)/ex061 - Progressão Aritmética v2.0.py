print('Gerador de PA')
print('=-=' * 10)
primeiro = int(input('Qual e o Primeiro Termo? '))
razao = int(input('Qual e a Razao? '))
termo = primeiro
posiçao = 1
while posiçao <= 10:
    print(termo, end=' -> ')
    termo += razao
    posiçao += 1

print('Acabou')

# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
