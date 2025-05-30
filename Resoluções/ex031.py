dist = float(input('Qual é a distância da sua viagem? '))
'''if dist <= 200:
    val = dist * 0.50
else:
    val = dist * 0.45'''
val = dist * 0.50 if dist <= 200 else dist * 0.45
print('Você está prestes a começar uma viagem de {}Km.'.format(dist))
print('E o preço da sua passagem será de R${:.2f}'.format(val))
