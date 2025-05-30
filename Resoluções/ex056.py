idades = 0
velho = 0
velhon = ''
mulher = 0
for c in range(1, 5):
    print('----- {} PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    idades += idade
    if c == 1 and sexo == 'M':
        velho = idade
        velhon = nome
    if sexo == 'M' and idade > velho:
        velho = idade
        velhon = nome
    if sexo == 'F' and idade < 20:
        mulher += 1
print('A média de idade do grupo é de {} anos'.format(idades / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, velhon))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))
