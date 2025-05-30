from math import hypot
cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
hip = hypot(cato, cata)
print('A hipotenusa vai medir {:.2f}'.format(hip))
