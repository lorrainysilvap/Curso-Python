#crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. considere U$1.00 = R$3,27.

real = float(input('quanto dinheiro você tem na carteira? R$'))
dólar = real/3.27
print('com R${:.2f} você pode comprar U${:.2f}'.format(real,dólar))
