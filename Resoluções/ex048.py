acu = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 ==0:
        acu += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, acu))
