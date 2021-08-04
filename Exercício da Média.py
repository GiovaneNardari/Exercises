print('CÁLCULO DA MÉDIA FINAL')
a1 = float(input('Digite a sua nota na avaliação 1: '))
a2 = float(input('Digite a sua nota na avaliação 2: '))
a3 = float(input('Digite a sua nota na avaliação 3 (digitar 0 caso não tenha feito): '))
mp = float(input('Digite a sua Média Prática: '))
if a3 == 0:
    mt = (0.4 * a1 + 0.6 * a2)
else:
    mt = max((0.4 * a1 + 0.6 * a3), (0.4 * a3 + 0.6 * a2))
if mt >= 5 and mp >= 5:
    mf = (0.5 * mt + 0.5 * mp)
    print(f'Aprovado com {mf}')
else:
    mf = min(mt, mp)
    print(f'Reprovado com {mf}')