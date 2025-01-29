#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

'''co = float(input('qual o comprimento do cateto oposto do triângulo retângulo? '))
ca = float(input('qual o comprimento do cateto adjacente do triângulo retângulo? '))
ch = (co ** 2 + ca ** 2) ** (1/2)
print ('a hipotenusa vai medir {:.2f}'.format(ch))'''

from math import hypot

co = float(input('qual o comprimento do cateto oposto? '))
ca = float (input('qual o comprimento do cateto adjacente? '))
ch = hypot(co,ca)
print('a hipotenusa vai medir{:.2f}'.format(ch))