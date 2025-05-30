opc = 's'
tot = 0
cont = 0
maior = 0
menor = 0
while opc == 's':
    n = int(input('Digite um número: '))
    cont += 1
    tot += n
    if cont == 1:
        maior = menor = n
    else:
        if  n > maior:
            maior = n
        if n < menor:
            menor = n
    opc = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
print('Você digitou {} números e a média foi {:.1f}'.format(cont, tot / cont))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
