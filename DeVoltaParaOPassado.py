list1 = []
list2 = []
list3 = []
while True:
    try:
        N = int(input('Digite o número de dias que possuem registro do preço das ações(Deve ser <=30): '))
        break
    except Exception:
        print('Erro no Input, tente novamente...')
        continue
while True:
    try:
        for i in range(N):
            valorA = float(input('Digite o valor diário das ações nesse período: '))
            list1.append(valorA)
        break
    except Exception:
        print('Erro no Input, tente novamente...')
        continue
while True:
    try:
        K = int(input('Indique o número máximo de dias desejado entre a compra e a venda das ações: '))
        Q = float(input('Indique a quantidade de dinheiro que será investida: '))
        break
    except Exception:
        print('Erro no Input, tente novamente...')
        continue
while True:
    try:
        for a in list1:
            for b in range(1, (K + 1)):
                par = [list1[(list1.index(a) + b)], a]
                list2.append(par)
    except Exception:
        continue
    finally:
        break
for c in range(len(list2)):
    dif = list2[c][0] - list2[c][1]
    if dif > 0:
        list3.append(dif)
    else:
        list3.append(0)
        continue
chosen = max(list3)
index = list3.index(chosen)
num = list2[index]
qnt = Q // num[1]
lucro = chosen * qnt
d_compra = list1.index(num[1]) + 1
d_venda = list1.index(num[0]) + 1
print(f'A compra das ações foi feita no dia {d_compra};')
print(f'O valor de compra das ações foi R$ {num[1]:.2f};')
print(f'A venda das ações foi feita no dia {d_venda};')
print(f'O valor de venda das ações foi R$ {num[0]:.2f};')
print(f'A quantidade de ações compradas foi {qnt};')
print(f'O lucro total foi de R$ {lucro:.2f};')

