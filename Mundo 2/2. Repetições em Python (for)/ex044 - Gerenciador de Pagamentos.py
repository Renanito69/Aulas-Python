'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto


– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' LOJA DO RENAN '))
preço = float(input('Qual e o valor da sua compra? ').title())
pagamento = int(
    input('''Qual e a forma de pagamento:
1 - Avista Dinheiro/Cheque: 10% De Desconto:
2 - Avista no Cartao: 5% De Desconto: 
3 - Em Ate 2x no cartao: Preço Normal: 
4 - 3x ou mais no Cartao: 20% De Juros:
5 - Cancelar: 
Escolha uma das Opçoes a cima: ''').title())
din = preço - (preço * (10/100))
car = preço - (preço * (5/100))
div = preço + (preço * (20/100))

if pagamento == 1:
    print('O valor da Compra de {} tera 10% De Desconto e Voce pagara {}'.format(
        preço, din).title())
elif pagamento == 2:
    print('O valor da Compra de {} tera 5% De Desconto e Voce pagara {}'.format(
        preço, car).title())
elif pagamento == 3:
    divi = preço / 2
    print('Sua Compra sera parcelada em 2x de {:.2f} SEM JUROS'.format(divi))
    print('O valor da compra de {} tera o valor normal'.format(preço).title())
elif pagamento == 4:
    x = int(input('Quantas vezes Voce deseja Parcelar? '))
    divi = div / x
    print('Sua Compra sera parcelada em {}x de {:.2f} COM JUROS'.format(x, divi))
    print('O valor da compra de {} tera 20% De juros e ficara {}'.format(
        preço, div).title())
elif pagamento == 5:
    print('O Pedido Esta Sendo Cancelado')
else:
    print('Essa Opçao Nao Existe')
