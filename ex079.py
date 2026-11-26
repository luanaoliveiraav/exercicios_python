lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)        
    res = 0
    res = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if res not in 'SN':
        print('Opção invalida')
    if res == 'N':
        break
print(lista)
n = []
n = set(lista)
sorted(n)
print(n)
