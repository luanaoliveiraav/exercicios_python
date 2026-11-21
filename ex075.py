n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

t = n1, n2, n3, n4
totpar = 0
for n in t:
    par = n % 2
    if par == 0:
        totpar += 1
        print(f'O {n} é par')
print(f'Ao todo são {totpar} números pares')
print(t.count(9))
print(t.index(3))
