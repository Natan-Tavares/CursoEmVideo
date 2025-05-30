n = int(input('''Digite um número para
Calcular seu Fatorial: '''))
fat = 1
cont = n
print('Calculando {}! = '.format(n), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(fat)
