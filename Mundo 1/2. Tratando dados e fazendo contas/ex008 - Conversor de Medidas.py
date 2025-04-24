# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('qual o valor em metro? '))
km = n / 1000
hm = n / 100
dam = n / 100
m = n
dm = n / 10
cm = n * 100
mm = n * 1000

print('o valor em:\n km: {} \n hm: {} \n dam: {} \n m:{} \n dm: {} \n cm: {}\n mm: {}'.format(
    km, hm, dam, m, dm, cm, mm))
