#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

n1 = str(input('primeiro aluno: '))
n2 = str(input('segunado aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))