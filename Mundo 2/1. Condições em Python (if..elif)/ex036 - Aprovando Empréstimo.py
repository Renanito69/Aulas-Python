casa = int(input('Qual e o Valor da Casa Que Deseja Comprar? '))
salario = int(input('Quanto Voce Recebe por Mes? '))
anos = int(input('Por Quantos Anos Voce Vai Querer Financiar a Casa? '))
minimo = salario * (30/100)  # Porcentagem do salario (Pt1)
prestaçao = casa / (anos * 12)

print('A Prestaçao sera de {:.2f}'.format(prestaçao))
if prestaçao > minimo:
    print('Desculpe mais o Imprestimo foi negado por ultrapaçar do 30% Do seu Salario')

else:
    print('Parabens o Impestimo foi Aprovado')

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
