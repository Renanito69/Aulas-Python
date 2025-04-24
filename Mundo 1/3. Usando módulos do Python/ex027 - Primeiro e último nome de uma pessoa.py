w = input('digite seu nome completo: ').strip()
s = w.split()
a = w.rsplit(maxsplit=1)

print('Seu Nome e: {}'.format(w))
print('Primeiro nome:', s[0])
print('Ultimo nome:', a[1])

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
