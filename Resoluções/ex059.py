from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opc = 0
while opc != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opc = int(input('>>>>> Qual é a sua opção? '))
    if opc == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
    elif opc == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
    elif opc == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
        else:
            print('Os valores são iguais')
    elif opc == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
