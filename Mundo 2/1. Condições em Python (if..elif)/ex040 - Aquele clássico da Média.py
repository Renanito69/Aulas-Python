w = float(input('Qual eo valor da 1 nota? '.title()))
s = float(input('qual eo valor da 2 nota? '.title()))
media = (w + s) / 2

print('Sua Nota foi {:.1f}'.format(media))
if media < 5:
    print('Reprovado!😢')
elif media <= 6.9:  # 7 > media >= 5: ou media >= 5 and media < 7:
    print('Recuperaçao!')
else:
    print('Aprovado!')
    print('Parabens ❤️')

# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO

# – Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO
