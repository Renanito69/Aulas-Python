import random

s = int(input('qual eo numero que estou pensando de 0 a 5? '))
w = random.randrange(5) #ou w = random.randint(0,5)
if w == s:
    print('voce acertou parabens')
else:
    print('ERROU MT BURRO SLC')
    print('o numero que eu estava pensando era {}'.format(w))

# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
