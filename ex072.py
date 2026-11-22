extenso = 'zero', 'um', 'dois', 'três', 'quatro',\
    'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',\
        'onze', 'doze', 'trese', 'quartoze', 'quinze',\
            'desesseis', 'desessete', 'desoito', 'desenove', 'vinte'
num = int(input('Digite um número entre 0 e 20:  '))
res = 0
while True:     
    if num >= 0 and num <= 20:
        indice = extenso[num]
        print(indice)        
        res = str(input('Quer continuar? [s/n] ')).strip().upper()[0]
    else:
            print('Opção invalida')
            num = int(input('Digite um número entre 0 e 20:  '))    
    if res == 'N':
        break
        if res != 'N' and res != 'S':
            print('Opção invalida')
    
   