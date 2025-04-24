# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    calc = larg * comp
    
    return print(f"A area de um terreno {larg} x {comp} é de {calc}m²")


print("-" * 30)
print("Controle de Terreno")
print("-" * 30)
largura = float(input("Qual e a largura do terreno: "))
comprimento = float(input("Qual e o comprimento do terreno: "))
area(larg=largura, comp=comprimento)
