par = 0
cont = 0
for i in range(1, 7):
    numero = int(input('Digite o {} Valor: '.format(i)))
    if numero % 2 == 0:
        par += numero
        cont += 1

print('A Soma dos {} Numeros pares e igual a {}'.format(cont, par))
