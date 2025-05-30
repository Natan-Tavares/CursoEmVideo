tot = 0
maismil = 0
barato = 0
cont = 0
bnome = ''
print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-'  * 30)
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    tot += preço
    cont += 1
    if preço > 1000:
        maismil += 1
    if cont == 1 or preço < barato:
        barato = preço
        bnome = nome
    opc = ' '
    while opc not in 'sn':
        opc = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if opc == 'n':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {maismil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {bnome} que custa R${barato:.2f}')
