frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
inv = frase[::-1]
print('O inverso de {} é {}'.format(frase, inv))
if frase == inv:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')
