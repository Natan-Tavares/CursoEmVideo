print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das comprasa: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    custo = preço - (preço * (10 / 100))
elif opção == 2:
    custo = preço - (preço * (5 / 100))
elif opção == 3:
    custo = preço
    parcela = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'. format(parcela))
elif opção == 4:
    custo = preço + (preço * (20 / 100))
    parcelas = int(input('Quantas parcelas? '))
    parcela = custo / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, parcela))
else:
    custo = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, custo))
