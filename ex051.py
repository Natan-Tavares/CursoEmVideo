print('=' * 30)
print('10 TERMOS DE UMA PA')
print('=' * 30)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = n1 + (10 - 1) * r
for pa in range(n1, d + r, r):
    print(pa, end=' ')
print('ACABOU')
