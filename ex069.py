maior = 0
h = 0
m20 = 0
while True:
    print('-' * 30)
    print('Cadastre uma pessoa')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F] ')).lower().strip()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'm':
        h += 1
    if sexo == 'f' and idade < 20:
        m20 += 1
    print('-' * 30)
    opc = ' '
    while opc not in 'sn':
        opc = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if opc == 'n':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {m20} mulheres com menos de 20 anos')
