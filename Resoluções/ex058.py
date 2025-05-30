from random import randint
tent = 0
print('Sou seu computador...')
print('Acabei de pensar em um número  entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
comp = randint(1, 10)
palp = 11
while palp != comp:
    palp = int(input('Qual é seu palpite? '))
    tent += 1
    if palp > comp:
        print('Menos... Tente mais uma vez.')
    elif palp < comp:
        print('Mais... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(tent))
