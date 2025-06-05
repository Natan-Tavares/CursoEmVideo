lista = list()
par = list()
impar = list()
resposta = ''
while resposta != 'n':
    n = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] ').strip().lower())
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A listaa de paares é {par}')
print(f'A lista de ímpares é {impar}')
