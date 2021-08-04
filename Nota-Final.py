while True:
    try:
        N = int(input('Indique a quantidade de avaliações realizadas: '))
        break
    except ValueError:
        print('Erro no input... Tente novamente!')
        continue

notas = []
for i in range(N):
    while True:
        try:
            nota = float(input('Digite suas notas: '))
            notas.append(nota)
            break
        except ValueError:
            print('Erro no input... Tente novamente!')
            continue

pesos = []
pesoTotal = 0
for x in range(N):
    while True:
        try:
            peso = int(input('Digite os pesos das avaliações, respectivas as notas digitadas anteriormente: '))
            pesos.append(peso)
            pesoTotal += peso
            break
        except ValueError:
            print('Erro no input... Tente novamente!')
            continue

soma = 0
for y in range(N):
    soma += notas[y] * pesos[y]

mean = soma / pesoTotal
if mean >= 5:
    print(f'\nSituação: Aprovado por nota!\nMédia nos Laboratórios: {mean}\nNota Final: {mean}')
elif mean <= 2.5:
    print(f'\nSituação: Reprovado por nota!\nMédia nos Laboratórios: {mean}\nNota Final: {mean}')
else:
    print('\nNotas insuficientes para aprovação...\n')
    while True:
        try:
            M = int(input('Indique quantos laboratórios serão utilizados para o exame: '))
            break
        except ValueError:
            print('Erro no input... Tente novamente!')
            continue

    pesos2 = []
    pesos2Total = 0
    for z in range(M):
        while True:
            try:
                peso2 = int(input('Indique quais pesos dos laboratórios serão utilizados no exame: '))
                pesos2.append(peso2)
                pesos2Total += peso2
                break
            except ValueError:
                print('Erro no input... Tente novamente!')
                continue

    exames = []
    for w in range(M):
        while True:
            try:
                exame = float(input('Indique a nota dos laboratórios selecionados para o exame: '))
                exames.append(exame)
                break
            except ValueError:
                print('Erro no input... Tente novamente!')
                continue

    somaExame = 0
    for v in range(M):
        somaExame += pesos2[v] * exames[v]

    meanExame = somaExame / pesos2Total
    notaFinal = min(5, (mean + meanExame) / 2)
    if notaFinal == 5:
        print(f'\nSituação: Aprovado por exame!\nMédia nos Laboratórios: {mean}\nNota Final: {notaFinal}')
    else:
        print(f'\nSituação: Reprovado no exame!\nMédia nos Laboratórios: {mean}\nNota Final: {notaFinal}')