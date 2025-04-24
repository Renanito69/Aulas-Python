soma = 0
cont = 0
for i in range(1, 500+1, 2):
    if i % 3 == 0:
        soma += i
        cont += 1
print('A soma dos {} numeros sao {:.2f}'.format(cont, soma))

# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
