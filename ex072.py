extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'trese', 'quartoze', 'quinze', 'desesseis', 'desessete', 'desoito', 'desenove', 'vinte'
num = int(input('Digite um número entre 0 e 20:  '))
if num > 0 and num < 20:
    indice = extenso[num]
    print(indice)
else:
    print('Opção invalida')
