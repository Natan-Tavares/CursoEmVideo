from random import randint
from time import sleep
num = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
numesc = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)
if numesc == num:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(num, numesc))
