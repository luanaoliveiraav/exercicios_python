t = (int(input('Digite um número: ')),\
      int(input('Digite um número: ')),\
        int(input('Digite um número: ')),\
            int(input('Digite um número: ')))
print(f'Você digitou os números: {t}')
print(f'Aou todo foi digitado {t.count(9)} números 9')
if 3 in t:
    print(f'O número três apareceu a primeira vez na {t.index(3)+1}º posição')
else:
    print('O 3 não foi digitado')
print('O números pares que foram digitado são: ', end='')
for n in t:
    par = n % 2
    if par == 0:
        print(n, end= ' ')
