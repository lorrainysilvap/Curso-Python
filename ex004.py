#faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas a s informaçoes possíveis sobre ela.

n=input('digite algo: ')
print('o tipo primitivo desse valor é: ', type(n))
print('só tem espaços? ', n.isspace())
print('é um número? ', n.isnumeric())
print('é alfabético? ', n.isalpha())
print('é alfanumérico? ', n.isalnum())
print('está em maiúsculas? ', n.isupper())
print('está em minúsculas? ', n.islower())
print('está capitalizada? ', n.istitle())
