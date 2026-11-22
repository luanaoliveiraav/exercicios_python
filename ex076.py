lista = ('arroz', 25.00), ('café', 14.00), ('açucar', 4.70), ('bisteca', 21.00), ('bolacha', 5.70)
print('-'*40)
print(f'{"Lista de compra":^40}')
print('-'*40)
for pro, pre in lista:
    print(f'{pro:.<30}\tR$ {pre:>5.2f}')
print('-'*40)
