sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    sal2 = sal + (sal * (15 / 100))
else:
    sal2 = sal + (sal * (10 / 100))
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, sal2))
