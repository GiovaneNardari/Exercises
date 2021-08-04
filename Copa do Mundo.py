# Variaveis necessarias
selecoes = []
partidas = []
dic = {}
caracteres = ["(", ")"]

for i in range(16):
    selecao = str(input('Insira o nome de um país participante: '))
    selecoes.append(selecao)
    dic[selecao] = {'partidas': 0, 'vitorias': 0, 'derrotas': 0, 'penaltis': 0,
                    'normal': 0, 'marcados': 0, 'sofridos': 0}

#leitura das partidas
print('Exemplo de como as partidas devem ser contabilizadas (com penaltis): Panama 4 x 4 (2 x 3) Suecia')
for x in range(16):
    partida1 = str(input('Contabilização da partida: '))
    partidas.append(partida1.split())

#processamento dos dados
for partida in partidas:
    if len(partida) == 8:
        selecao1 = partida[0]
        selecao2 = partida[7]
        dic[f'{selecao1}']['partidas'] += 1
        dic[f'{selecao2}']['partidas'] += 1
        dic[f'{selecao1}']['penaltis'] += 1
        dic[f'{selecao2}']['penaltis'] += 1
        dic[f'{selecao1}']['marcados'] += int(partida[1])
        dic[f'{selecao2}']['marcados'] += int(partida[3])
        dic[f'{selecao1}']['sofridos'] += int(partida[3])
        dic[f'{selecao2}']['sofridos'] += int(partida[1])
        if int(partida[4].lstrip("(")) > int(partida[6].rstrip(")")):
            dic[f'{selecao1}']['vitorias'] += 1
            dic[f'{selecao2}']['derrotas'] += 1
        elif int(partida[6].rstrip(")")) > int(partida[4].lstrip("(")):
            dic[f'{selecao1}']['derrotas'] += 1
            dic[f'{selecao2}']['vitorias'] += 1

    elif len(partida) == 5:
        selecao1 = partida[0]
        selecao2 = partida[4]
        dic[f'{selecao1}']['partidas'] += 1
        dic[f'{selecao2}']['partidas'] += 1
        dic[f'{selecao1}']['normal'] += 1
        dic[f'{selecao2}']['normal'] += 1
        dic[f'{selecao1}']['marcados'] += int(partida[1])
        dic[f'{selecao2}']['marcados'] += int(partida[3])
        dic[f'{selecao1}']['sofridos'] += int(partida[3])
        dic[f'{selecao2}']['sofridos'] += int(partida[1])
        if int(partida[1]) > int(partida[3]):
            dic[f'{selecao1}']['vitorias'] += 1
            dic[f'{selecao2}']['derrotas'] += 1
        elif int(partida[3]) > int(partida[1]):
            dic[f'{selecao1}']['derrotas'] += 1
            dic[f'{selecao2}']['vitorias'] += 1

# Saída de dados
for selecao in selecoes:
    if dic[f'{selecao}']["derrotas"] == 0:
        campeao = selecao
    print("-" * 50)
    print("Pais:", selecao)
    print("Partidas:", dic[f'{selecao}']["partidas"])
    print("Partidas decididas em tempo normal de jogo:", dic[f'{selecao}']["normal"])
    print("Partidas decicidas nos penaltis:", dic[f'{selecao}']["penaltis"])
    print("Vitorias:", dic[f'{selecao}']["vitorias"])
    print("Derrotas:", dic[f'{selecao}']["derrotas"])
    print("Gols marcados:", dic[f'{selecao}']["marcados"])
    print("Gols sofridos:", dic[f'{selecao}']["sofridos"])
print("-" * 50)
print(f'Seleção campeã: {campeao}')