time = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
        'São Paulo', 'Fluminense', 'Sport Recife',
        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
        'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {time}')
print('-=' * 15)
print(f'Os 5 primeiros são {time[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {time[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(time)}')
print('-=' * 15)
print(f'O Chapecoense está na {time.index("Chapecoense") + 1} posição')
