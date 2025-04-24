'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  Ex:                                                                                                                                                                        escreva(‘Olá, Mundo!’) Saída:   

~~~~~~~~~~~~
"Ola Mundo"
~~~~~~~~~~~~'''

def escreva(palavra):
    leia = palavra.center(len(palavra) * 2)
    print("~" * len(palavra) * 2)
    print(leia)
    print("~" * len(palavra) * 2)


escrita = str(input("Digite algo: "))
escreva(palavra=escrita)
