n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
menor = n1
maior = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
