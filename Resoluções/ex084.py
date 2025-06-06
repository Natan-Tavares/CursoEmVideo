lista1 = []
lista2 = []
maior = menor = 0
resposta = ''
while resposta != 'n':
    lista1.append(str(input('Nome: ')))
    lista1.append(float(input('Peso: ')))
    if len(lista2) == 0:
        maior = menor = lista1[1]
    else:
        if lista1[1] > maior:
            maior = lista1[1]
        if lista1[1] < menor:
            menor = lista1[1]
    lista2.append(lista1[:])
    lista1.clear()
    resposta = str(input('Quer continuar [S/N] ')).strip().lower()
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(lista2)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for i in lista2:
    if i[1] == maior:
        print(f'[{i[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for i in lista2:
    if i[1] == menor:
        print(f'[{i[0]}] ', end='')
print()
