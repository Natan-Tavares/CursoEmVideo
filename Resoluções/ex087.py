matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
coluna3 = 0
par = 0
cont = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l][c] = n
        if n % 2 == 0:
            par += n
    coluna3 += n
linha2 = max(matriz[1])
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {linha2}')
