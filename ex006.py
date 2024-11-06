#crie um algoritmo que leia um num e mostre seu dobro, triplo e raiz quadrada.

n=int(input('digite um número: '))
d=n*2
t=n*3
r=n**(1/2)
print('o dobro de {} é {}, o triplo é {} e a raiz quadrada {:.2f}'.format(n,d,t,r))
