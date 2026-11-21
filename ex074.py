import random
num = tuple(random.sample(range(1, 101), 5))
maior = menor = 0
for cont in num:
    if maior == 0:
        maior = cont
    elif menor == 0:
        menor = cont
    if cont >= maior:
        maior = cont
    elif cont < menor:
        menor = cont
print(num)
print(f'O maior número é {maior} e o menor é {menor}')
