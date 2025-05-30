n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores {n}')
nove = n.count(9)
print(f'O valor 9 apareceu {nove} vezes')
if 3 in n:
    tres = n.index(3)
    print(f'O valor 3 apareceu na {tres + 1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
