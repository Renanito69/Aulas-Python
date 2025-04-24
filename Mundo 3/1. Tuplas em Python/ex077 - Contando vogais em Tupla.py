'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
#Corrigido
for n in palavras:
    print(f'\nNa palavra {n.upper()} temos as vogais ', end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
#Como eu Fiz
# vogais = 'aeiou'

    # for n in palavras:
    #     v = ''
    #     for letra in n:
    #         if letra in vogais:
    #             v += ' ' + letra
    #     print(f'Na palavra {n.upper()} temos as vogais {v.upper()}')
