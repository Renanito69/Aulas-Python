# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cor_verm = '\033[31m' # Vermelha
cor_verd = '\033[32m' # Verde
cor_amar = '\033[33m' # Amarelo
cor_roxo = '\033[35m' # Roxo
cor_azul = '\033[34m' # Azul
sem_cor = '\033[m' # Tirar A Cor
quant = 0 # Quantas Vezes Ele foi Divisivel
primo = int(input('Escolha Um Numero: '))
for i in range(1, primo+1):
    if primo % i == 0:
        print('{}{}{}'.format(cor_verd, i, sem_cor), end=' ')
        quant += 1
    else:
        print('{}{}{}'.format(cor_verm, i, sem_cor), end=' ')

print('\nO Numero {} Foi Divisivel {} vezes'.format(primo, quant))
if quant == 2:
    print('Por isso ele {}E{} {}PRIMO'.format(cor_azul, sem_cor, cor_amar))
else:
    print('Por isso ele {}NAO{} E {}PRIMO'.format(cor_roxo, sem_cor, cor_amar))
