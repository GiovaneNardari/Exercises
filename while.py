#1lb=0,454kg
print('TABELA DE CONVERSÃO DE LIBRAS PARA QUILOGRAMAS')
print('='*44)
print('Libras\tKg')
a = 1
b = 0.454
print(f'{a:3}\t{b:7.3f}') 
k = 5
while k <= 100:
    print(f'{k:3}\t{k * 0.454:7.3f}')
    k += 5
print('<<<FIM>>>')
