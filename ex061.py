print('Gerador de PA')
print('-=' * 10)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = n1
pos = 1
while pos <= 10:
    print('{}'.format(cont), end=' ')
    cont += r
    pos += 1
print('FIM')
