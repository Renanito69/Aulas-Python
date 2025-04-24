import random

n = input('escreva um nome: ')
n2 = input('escreva o 2 nome: ')
n3 = input('escreva o 3 nome: ')
n4 = input('escreva o 4 nome: ')
s = [n, n2, n3, n4]
random.shuffle(s)
print(s)

# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
