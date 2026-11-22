times = 'Flamengo', 'Palmeiras', 'Cruzeiro', 'Fluminense', 'Atlético-PR', 'Bahia', 'Atlético-MG', 'Santos', 'Bragantino', 'São Paulo', 'Vasco', 'Botafogo', 'Coritiba', 'Marisol', 'Corinthias', 'Vitória', 'Internacional', 'grêmio', 'Remo', 'Chapecoense'
print(f'Os cincos primeiros colocado no Campeonato Brasileiro 2026 são: {times[:5]}')
print(f'Os quatro últimos colocados são: {times[-4:]}')
print(f'Os time em ordem alfabetica são: {sorted(times)}')
print(f'O Corinthis esta na posição {times.index('Corinthias')+1}º')

for pos, time in enumerate(times):
    if time == 'Chapecoense':
        print(f'A {time} se encontra na posição {pos + 1}')
