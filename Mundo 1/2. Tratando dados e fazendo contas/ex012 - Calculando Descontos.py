n = float(input('qual eo valor da compra? R$'))
n2 = float(input('qual o valor do desconto? '))
s = n2 * n
s2 = s / 100
s3 = n - s2

print('o valor que voce pagara e R${:.2f} com desconto de {} num obj de {} valor'.format(
    s3, n2, n))

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
