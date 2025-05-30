resposta = 's'
lista = list()
while resposta == 's':
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    resposta = str(input('Quer continuar? [S/N] ').lower().strip())
print('-=' * 30)
lista.sort()
print(f'Você digitou os valores {lista}')
