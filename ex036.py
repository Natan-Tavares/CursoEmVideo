casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))
prest = casa / (ano * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, ano, prest))
if prest > sal * 30 / 100:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
