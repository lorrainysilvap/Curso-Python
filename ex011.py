#faça um programa que leia a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
área = larg*alt
print('sua parede tem a a dimensão de {}x{} e sua área é de {}m²'.format(larg,alt,área))
tinta = área/2
print('para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))