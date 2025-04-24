n1 = int(input ('degite um numero: '))
n2 = int(input ('digite o segundo numero: '))
s = n1 + n2
cor = '\033[33m'
sem = '\033[m'
#print('a soma e {}' .format(s))
#print('a soma entre', n1, 'e', n2, 'e', s)
print('a soma entre {}{}{} e {}{}{} e {}{}{}' .format(cor, n1, sem, cor, n2, sem, '\033[32m', s, sem ))