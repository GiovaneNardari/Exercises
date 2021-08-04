classe = []
menu = 3
while True:
    try:
        total = int(input('Digite o número de alunos na sala: '))
        break
    except Exception:
        print('Erro na digitação, tente novamente...')
        continue
for n in range(total):
    while True:
        try:
            aluno = str(input('Digite o nome do aluno: '))
            nota = float(input(f'Digite a nota do {aluno} na prova: '))
            ra = int(input(f'Digite o R.A do {aluno}: '))
            classe.append([aluno, ra, nota])
            break
        except Exception:
            print('Erro na digitação, tente novamente...')
            continue
while menu != 0:
    print(' << << < MENU >> >> >')
    print('1. Consultar a nota de um aluno')
    print('2. Modificar a nota de um aluno')
    print('3. Imprimir lista de alunos completa (no formato [Aluno, R.A, Nota]')
    print('0. Sair do Programa')
    while True:
        try:
            menu = int(input('Digite o código correspondente à ação que deseja: '))
            break
        except Exception:
            print('Erro na digitação, tente novamente...')
            continue
    if menu == 1:
        while True:
            try:
                pesq = int(input('Digite o R.A do aluno que deseja consultar a sua respectiva nota: '))
                break
            except Exception:
                print('Erro na digitação, tente novamente...')
                continue
        for a in range(0, len(classe)):
            raConsultado = classe[a][1]
            if raConsultado == pesq:
                alunoConsultado = classe[a][0]
                notaConsultado = classe[a][2]
                print(f'A nota do(a) {alunoConsultado} foi {notaConsultado}!')
                break
            else:
                continue
    elif menu == 2:
        while True:
            try:
                pesq = int(input('Digite o R.A do aluno que deseja alterar a sua respectiva nota: '))
                break
            except Exception:
                print('Erro na digitação, tente novamente...')
                continue
        for a in range(0, len(classe)):
            raConsultado = classe[a][1]
            if raConsultado == pesq:
                alunoConsultado = classe[a][0]
                notaConsultado = classe[a][2]
                print(f'A nota do(a) {alunoConsultado} foi {notaConsultado}!')
                while True:
                    try:
                        notaNova = float(input(f'Digite a nova nota para o(a) {alunoConsultado}: '))
                        break
                    except Exception:
                        print('Erro na digitação, tente novamente...')
                        continue
                classe[a].pop(2)
                classe[a].insert(2, notaNova)
                print(f'A nota do(a) {alunoConsultado} agora é {notaNova}!')
            else:
                continue
    elif menu == 3:
        print(classe)
    elif menu == 0:
        print('<<<<<Fim do Programa>>>>>')
        break
    else:
        print('Código inválido, por favor tente novamente...')
        continue
