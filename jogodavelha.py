#Atividade Avaliativa - A2
#Giovane Bruno Nardari
#RA = 21000244

#funções
def exibir_matriz():  #Exibição da grade
    print('='*33)
    print('<<<< J O G O  D A  V E L H A >>>>')
    print('=' * 33)
    print()
    print(f' {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]}')
    print('-'*11)
    print(f' {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]}')
    print('-'*11)
    print(f' {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]}')
    print()

def jogadas(position, marca):  #Contabilização das jogadas
    linha = (position - 1) // 3
    coluna = (position - 1) % 3
    if type(matriz[linha][coluna]) != int:
        print('JOGADA INVÁLIDA, jogue apenas em posições não ocupadas...')
        print()
        return True
    else:
        matriz[linha][coluna] = marca
        return False

def check():  #Busca possível vitória
    for a in range(3):
        if matriz[a][0] == matriz[a][1] and matriz[a][0] == matriz[a][2]:
            victory = [True, matriz[a][0]]
            return victory
        elif matriz[0][a] == matriz[1][a] and matriz[0][a] == matriz[2][a]:
            victory = [True, matriz[0][a]]
            return victory
    if matriz[1][1] == matriz[0][0] and matriz[1][1] == matriz[2][2]:
            victory = [True, matriz[1][1]]
            return victory
    elif matriz[1][1] == matriz[0][2] and matriz[1][1] == matriz[2][0]:
            victory = [True, matriz[1][1]]
            return victory
    else:
        victory = [False, 0]
        return victory

def fim(marca): #Exibição do vencedor
    if marca == 'X':
        print('PARABÉNS Jogador 1, Você venceu o Jogo da Velha!')
        print()
    else:
        print('PARABÉNS Jogador 2, Você venceu o Jogo da Velha!')
        print()

#principal
continuar = True

while continuar == True:
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #Criação ou Redefinição da Matriz
    r = 0

    for i in range(1, 10):
        r += 1
        exibir_matriz()
        victory = check()
        if victory[0] == True:
            fim(victory[1])
            break

        elif i % 2 != 0:
            while True:
                jogada = int(input(f'Jogador 1 (X), digite uma posição não ocupada para jogar: ')) #digitação da jogada
                print()
                simbolo = 'X'
                if jogadas(jogada, simbolo) == False:
                    break
                else:
                    continue

        elif i % 2 == 0:
            while True:
                jogada = int(input(f'Jogador 2 (O), digite uma posição não ocupada para jogar: ')) #digitação da jogada
                print()
                simbolo = 'O'
                if jogadas(jogada, simbolo) == False:
                    break
                else:
                    continue

    if r == 9:
        print('O jogo terminou empatado... DEU VELHA!')

    jogar = input('Deseja jogar novamente?(S/N): ') #possibilidade de reiniciar o jogo
    print()

    if jogar == 'S':
        continuar = True
    else:
        print('Fim do Programa!')
        continuar = False