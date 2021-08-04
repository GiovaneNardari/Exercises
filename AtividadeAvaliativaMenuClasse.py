# Atividade Avaliativa:
# Aluno: Giovane Bruno Nardari
# RA: 21000244
classe = []
menu = 3
rel = 3
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
            aluno = str(input('Digite o nome do(a) aluno(a): '))
            nota = float(input(f'Digite a nota do(a) {aluno.title()} na prova: '))
            ra = int(input(f'Digite o R.A do(a) {aluno.title()}: '))
            for a in range(total):
                if ra == classe[a][1]:
                    print(f'O R.A: {ra} já está cadastrado!')
                    ra = int(input(f'Digite outro R.A para o(a) {aluno.title()}: '))
                    continue
                else:
                    break
            classe.append([aluno, ra, nota])
            break
        except IndexError:
            classe.append([aluno, ra, nota])
            break
        except ValueError:
            print('Erro na digitação, tente novamente...')
            continue
while menu != 0:
    if rel == 0:
        print('<<<<<Fim do Programa>>>>>')
        break
    print(
        f'\nTotal de alunos cadastrados: {total}\n'
        '\n<<<<<<<<<<<<<OPERAÇÕES>>>>>>>>>>>>>\n'
        '1. Incluir um(a) aluno(a)\n'
        '2. Modificar a nota de um aluno\n'
        '3. Excluir um(a) aluno(a)\n'
        '4. Relatórios\n'
        '0. Sair do programa\n')
    if total == 0:
        print(
            'ATENÇÃO: Não há alunos cadastrados!\n'
            'Só é possível: 1. Incluir um(a) novo(a) aluno(a) ou 0. Sair do programa!\n')
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
                aluno = str(input('Digite o nome do(a) novo(a) aluno(a): '))
                nota = float(input(f'Digite a nota do(a) {aluno.title()} na prova: '))
                ra = int(input(f'Digite o R.A do(a) {aluno.title()}: '))
                classe.append([aluno, ra, nota])
                total += 1
                break
            except Exception:
                print('Erro na digitação, tente novamente...')
                continue
    elif menu == 2:
        while True:
            try:
                pesq = int(input('Digite o R.A do(a) aluno(a) que deseja alterar a sua respectiva nota: '))
                print(
                    'ATENÇÃO: Caso o R.A digitado não seja encontrado,'
                    ' você será redirecionado novamente para o menu de Operações!')
                break
            except Exception:
                print('Erro na digitação, tente novamente...')
                continue
        for a in range(0, len(classe)):
            raConsultado = classe[a][1]
            if raConsultado == pesq:
                alunoConsultado = classe[a][0]
                notaConsultado = classe[a][2]
                print(f'A nota do(a) {alunoConsultado.title()} foi {notaConsultado}!')
                while True:
                    try:
                        notaNova = float(input(f'Digite a nova nota para o(a) {alunoConsultado.title()}: '))
                        break
                    except Exception:
                        print('Erro na digitação, tente novamente...')
                        continue
                classe[a].pop(2)
                classe[a].insert(2, notaNova)
                print(f'A nota do(a) {alunoConsultado.title()} agora é {notaNova}!')
            else:
                continue
    elif menu == 3:
        while True:
            try:
                pesq = int(input('Digite o R.A do(a) aluno(a) que deseja remover da lista dos alunos: '))
                print(
                    'ATENÇÃO: Caso o R.A digitado não seja encontrado,'
                    ' você será redirecionado novamente para o menu de Operações!')
                for a in range(0, len(classe)):
                    raConsultado = classe[a][1]
                    if raConsultado == pesq:
                        classe.pop(a)
                        total = total - 1
                        print('\nO Aluno foi removido com sucesso!')
                        break
                    else:
                        continue
                break
            except Exception:
                print('Erro na digitação, tente novamente...')
                continue
    elif menu == 4:
        while rel != 0:
            print(
                '<<<<<<<<RELATÓRIOS>>>>>>>>\n'
                '1. Imprimir dados de um(a) aluno(a)\n'
                '2. Imprimir lista de alunos completa (no formato [Aluno, R.A, Nota]\n'
                '3. Voltar ao menu principal\n'
                '0. Sair do Programa\n')
            while True:
                try:
                    rel = int(input('Digite o código correspondente à ação que deseja: '))
                    break
                except Exception:
                    print('Erro na digitação, tente novamente...')
                    continue
            if rel == 1:
                while True:
                    try:
                        pesq = int(input('Digite o R.A do(a) aluno(a) que deseja consultar a sua respectiva nota: '))
                        print(
                            'ATENÇÃO: Caso o R.A digitado não seja encontrado,'
                            ' você será redirecionado novamente para o menu de Relatórios!')
                        break
                    except Exception:
                        print('Erro na digitação, tente novamente...')
                        continue
                for a in range(0, len(classe)):
                    raConsultado = classe[a][1]
                    if raConsultado == pesq:
                        alunoConsultado = classe[a][0]
                        notaConsultado = classe[a][2]
                        print(f'\nA nota do(a) {alunoConsultado.title()}, portador(a) do R.A= {raConsultado}, foi {notaConsultado}!\n')
                        break
                    else:
                        continue
            elif rel == 2:
                print('<<<<<LISTA DE ALUNOS COMPLETA>>>>>')
                for a in range(0, len(classe)):
                    alunoConsultado = classe[a][0]
                    raConsultado = classe[a][1]
                    notaConsultado = classe[a][2]
                    print(
                        f'Nome: {alunoConsultado.title():<}\n'
                        f'R.A:  {raConsultado:<}\n'
                        f'Nota: {notaConsultado:<}\n'
                        '==================================\n')
            elif rel == 3:
                break
            elif rel == 0:
                break
            else:
                print('Código inválido, por favor tente novamente...')
                continue
    elif menu == 0:
        print('<<<<<Fim do Programa>>>>>')
        break
    else:
        print('Código inválido, por favor tente novamente...')
        continue
