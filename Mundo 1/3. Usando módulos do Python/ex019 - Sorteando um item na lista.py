import random

n = input('escreva o nome: ')
n2 = input('escreva o 2 nome: ')
n3 = input('escreva o 3 nome: ')
n4 = input('escreva o 4 nome: ')

n = [n, n2, n3, n4]
random.shuffle(n)
print(n)

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
