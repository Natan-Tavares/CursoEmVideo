from random import randint
cont = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
while True:
    jogador = int(input('Diga um valor: '))
    pi = ' '
    computador = randint(0, 11)
    total = jogador + computador
    print('-' * 30)
    while pi not in 'pi':
        pi = str(input('Par ou Ímpar? [P/I] ')).lower().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if total % 2 == 0:
        print('-' * 30)
        if pi == 'p':
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif total % 2 == 1:
        print('-' * 30)
        if pi == 'p':
            print('Você PERDEU!')
            break
        else:
            print('Você VENCEU!')
            cont += 1
    print('=-' * 15)
    print('Vamos jogar novamente...')
print('=-' * 15)
print(f'GAME OVER! Você venceu {cont} vezes.')
