base = float(input('Comprimento da base: '))
altura = float(input('Comprimento da altura: '))
area = base * altura
if base == altura:
    print(f'Area do Quadrado = {area: .2f}')
else:
    print(f'Area do Retangulo = {area: .2f} ')
