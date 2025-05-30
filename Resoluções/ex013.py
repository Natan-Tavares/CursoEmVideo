sal = float(input('Qual é o salário do funionário? R$'))
aum = sal + (sal * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber {:.2f}'.format(sal, aum))
