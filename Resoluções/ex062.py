print('Gerador de PA')
print('-=' * 10)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = n1
pos = 1
max = 0
mais = 10
while mais != 0:
    max += mais
    while pos <= max:
        print('{}'.format(cont), end=' ')
        cont += r
        pos += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(max))
