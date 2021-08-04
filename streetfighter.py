hp_ryu = int(input('HP inicial do Ryu: '))
hp_ken = int(input('HP inicial do Ken: '))
ryu_golpe = 0
ken_golpe = 0

while hp_ryu > 0 and hp_ken > 0:
    golpe = int(input('Insira o dano causado pelo golpe(valor negativo caso seja um golpe do ken): '))
    if golpe > 0:
        print(f'Ryu acertou um golpe que causou {golpe} de dano em Ken!')
        ryu_golpe += 1
        hp_ken = hp_ken - golpe
        if (hp_ken <= 0) is False:
            print(f'HP de Ken no momento é {hp_ken}')
            print(f'HP de Ryu no momento é {hp_ryu}')
        else:
            print('Ryu foi o vencedor da luta!')
            print(f'Ryu aplicou {ryu_golpe} golpe(s) em Ken!')
            print(f'Ken aplicou {ken_golpe} golpe(s) em Ryu antes de perder...')
            print(f'HP final de Ken foi 0')
            print(f'HP final de Ryu foi {hp_ryu}')
    elif golpe < 0:
        golpe = golpe * (-1)
        print(f'Ken acertou um golpe que causou {golpe} de dano em Ryu!')
        hp_ryu = hp_ryu - golpe
        ken_golpe += 1
        if (hp_ryu <= 0) is False:
            print(f'HP de Ryu no momento é {hp_ryu}')
            print(f'HP de ken no momento é {hp_ken}')
        else:
            print('Ken foi o vencedor da luta!')
            print(f'Ken aplicou {ken_golpe} golpe(s) em Ryu!')
            print(f'Ryu aplicou {ryu_golpe} golpe(s) em Ken antes de perder...')
            print(f'HP final de Ryu foi 0')
            print(f'HP final de Ken foi {hp_ken}')
    else:
        print('O golpe aplicado causou 0 de dano...')