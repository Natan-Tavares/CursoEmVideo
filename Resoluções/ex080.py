lista = []
pos = 0
for i in range(5):
    n = int(input('Digite um número: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-=' * 30)
print(f'Os valores foram: {lista}')
