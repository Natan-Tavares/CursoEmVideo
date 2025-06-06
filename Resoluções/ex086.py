lista1 = []
lista2 = []
cont = 0
for i in range(0, 3):
    for j in range(0, 3):
        lista1.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
    lista2.append(lista1[:])
    lista1.clear()
print('-=' * 30)
for i in lista2:
    print(lista2[cont])
    cont += 1
