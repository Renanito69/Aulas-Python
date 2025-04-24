from datetime import date
w = int(input('coloque um ano para saber se e BISSEXTO e 0 para o ano que esta: '))
if w == 0:
    w = date.today().year
elif w % 4 == 0 and w % 100 != 0 or w % 400 == 0:
    print('o ano {} e BISSEXTO'.format(w))
else:
    print('o ano {} NAO e BISSEXTO'.format(w))

# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
