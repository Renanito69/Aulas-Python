print('Gerador de PA')
print('=-=' * 10)
primeiro = int(input('Qual e o Primeiro Termo? '))
razao = int(input('Qual e a Razao? '))
tempo = 0
termo = 10
total = 0

while termo != 0:
    total += termo
    while tempo < total:
        print('{} --> '.format(primeiro), end='')
        primeiro += razao
        tempo += 1
    print('PAUSA')
    print('Digite 0 para sair')
    termo = int(input('Deseja adicionar mais numeros: '))

print('Fim')

# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
