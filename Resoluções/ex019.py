from random import choice
pa = input('Primeiro aluno: ')
sa = input('Segundo aluno: ')
ta = input('Terceiro aluno: ')
qa = input('Quarto aluno: ')
al = [pa, sa, ta, qa]
esc = choice(al)
print('O aluno escolhido foi {}'.format(esc))
