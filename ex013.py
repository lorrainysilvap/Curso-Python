#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input('qual o salário do funcionário? R$ '))
novoS = salário + (salário * 15/100)
print('o funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário,novoS))
