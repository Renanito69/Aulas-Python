primeiro = int(input('Qual e o Primeiro Termo '))
razao = int(input('Qual e a Razao? '))
a = 0
print('A Progressao Aritimetica E')
for pa in range(10):
    a += 1
    soma = primeiro + razao * (a - 1)
    print(soma,  end=' -> ')
print('Fim')

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
