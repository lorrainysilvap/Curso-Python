#escreva um programa que leia o valor em metros e exiba convertido em centímetros e milímetros.

m=float(input('digite o valor em metros a ser convertido: '))
c=m*100
mm=m*1000
print('o valor em metro {}m convertido em\ncentímetros: {:.0f}c\nmilímetros: {:.0f}mm'.format(m,c,mm))
