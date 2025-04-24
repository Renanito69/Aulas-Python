# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('escreva algo: ')



print('o tipo primitivo dele e ', type(n))
print('aqui e tudo minusculo: ', n.islower())
print('aqui e letras: ', n.isalpha())
print('aqui e quando tem espaço: ', n.isspace())
print('aqui e quando tem numero: ', n.isnumeric())
print('aqui e quando tem numero e letras: ', n.isalnum())
print('aqui e tudo em maiusculo: ', n.isupper())
print('começa com maiuscula: ', n.istitle())