vel = int(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    mult = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(mult))
print('Tenha um bom dia! Dirija com segurança!')
