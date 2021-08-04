d = float(input('Insira o diâmetro do tanque de transporte, em metros: '))
h = float(input('Insira a altura do tanque de transporte, em metros: '))
a = float(input('Insira a capacidade de armazenamento do posto A, em litros: '))
b = float(input('Insira a capacidade de armazenamento do posto B, em litros: '))
c = float(input('Insira a capacidade de armazenamento do posto C, em litros: '))
pi = 3.14
tanque = 1000 * pi * h * ((d / 2) ** 2)
if tanque >= a:
    tanque = tanque - a
    print('Posto A foi reabastecido.')
else:
    print('Posto A não foi reabastecido')
if tanque >= b:
    tanque = tanque - b
    print('Posto B foi reabastecido')
else:
    print('Posto B não foi reabastecido')
if tanque >= c:
    tanque = tanque - c         #não é necassário, uma vez que c é o último posto
    print('Posto C foi reabastecido')
else:
    print('Posto C não foi reabastecido')
