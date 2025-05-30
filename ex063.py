print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
termos = int(input('Quantos termos você quer mostrar? '))
cont = 3
n1 = 0
n2 = 1
print('~' * 30)
print(n1, n2, end=' ')
while cont <= termos:
    n3 = n1 + n2
    print(n3, end=' ')
    cont += 1
    n1 = n2
    n2 = n3
print('FIM')
print('~' * 30)
