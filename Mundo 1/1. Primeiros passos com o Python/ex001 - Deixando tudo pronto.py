# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('digite seu nome: ').upper

print('e um prazer te conhecer, {}{}{}!!!'.format('\033[1;35m', nome, '\033[m'))