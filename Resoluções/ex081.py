lista = list()
resposta = ''
while resposta != 'n':
    n = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [S/N] ').strip().lower())
    lista.append(n)
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
