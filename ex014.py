# escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('informe a temperatura em °C: '))
f = c * 9/5 + 32
print(' a temperatura de {}°C corresponde a {}°F'.format(c,f))

