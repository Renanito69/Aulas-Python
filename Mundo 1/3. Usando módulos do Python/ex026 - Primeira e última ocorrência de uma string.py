w = str(input('digite algo: ')).lower().strip()

# print('1: tem ', s.count('a'))
print('1: a letra A aparece {} vezes na frase'.format(w.count('a')))
#print('2: ela aparece a primeira vez na posiçao ', s.find('a'))
print('2: a letra A aparece pela primeira vez na posiçao {}'.format(w.find('a')+1))
#print('3: e termina na posiçao ', s.rfind('a'))
print('3: a letra A termina na posiçao {}'.format(w.rfind('a')+1))

# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
