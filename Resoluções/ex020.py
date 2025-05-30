from random import shuffle
pa = input('Primeiro aluno: ')
sa = input('Segundo aluno: ')
ta = input('Terceiro aluno: ')
qa = input('Quarto aluno: ')
al = [pa, sa, ta, qa]
shuffle(al)
print('A ordem de apresentação será')
print(al)
