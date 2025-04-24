import math
n = float(input('qual e o angulo? '))
# n2 = int(input('valo do cateto oposto? '))
# n3 = int(input('valo do cateto adjesente? '))
# c = n2 ** 2
# c2 = n3 ** 2
# s = c + c2
# r = math.sqrt(s)
# seno = n2 / r
# cos = n3 / r
# tan = n2 / n3
seno = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))

print('o valor de seno {:.2f}\n o valor de cosseno {:.2f}\n o valor de tangente {:.2f}'.format(
    seno, cos, tan))

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
