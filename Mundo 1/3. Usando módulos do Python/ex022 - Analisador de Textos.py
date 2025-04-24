# len Quantas letra tem
# upper MAIUSCULO
# lower minusculo
# split pra seperar cada uma
s = str(input('Digite seu Nome: '))
a = s.replace(' ', '')
w = s.split()
f = len(w[0])

print('1:', 'Nome com todas as letras MAIUSCULAS:')
print(s.upper())
print('2:', 'Nome com todas as letras minusculas: ')
print(s.lower())
print('3:', 'Quantas letras tem o seu nome sem os espeços')
print(len(a))
print('4:', 'Quantas letras tem o 1 nome?')
print(f)

# Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo(sem considerar espaços).
