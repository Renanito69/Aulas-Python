# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = input("Digite a expressão")
lista = []
for letra in expressao:
    if letra == '(':
        lista.append('(')
    elif letra == ')':
        if len(letra) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão esta valida')
else:
    print("Sua expressão esta errada")
