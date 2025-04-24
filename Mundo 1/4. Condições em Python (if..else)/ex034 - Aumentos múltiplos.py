w = int(input('Qual salario voce recebe? '))
s = w * (10/100)
s2 = w + s
n = w * (15/100)
n2 = w + n

if w >= 1251:
    print('Voce rebera um aumento de 10 porcento do salario')
    print('agora voce recebera R${:.2f}'.format(s2))
else:
    print('o seu salario e inferior a 1250 por isso voce recebera 15 porcento')
    print('seu novo salario sera de R${:.2f}'.format(n2))

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
