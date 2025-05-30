n = int(input('Digite um número para ver sua tabuada: '))
for tabu in range(1, 11):
    print('{} X {:2} = {}'.format(n, tabu, n * tabu))
