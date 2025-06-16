from random import randint
from time import sleep
lista = []
resultados = []
print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0, jogos):
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    resultados.append(lista[:])
    lista.clear()
print(f'-=-=-= SORTEANDO {jogos} JOGOS -=-=-=')
for i, j in enumerate(resultados):
    print(f'Jogo {i + 1}: {j}')
    sleep(1)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')