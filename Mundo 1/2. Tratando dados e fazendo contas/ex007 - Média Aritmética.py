# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n = float(input('qual a 1 nota? '))
n2 = float(input('qual a 2 nota? '))

s = n + n2
m = s / 2

print('a soma das notas e {} ea media delas e {:.1f}'.format(s, m))
