n1 = int(input('Digite o primeiro número da sua sequência: '))
n3 = int(input('Digite o terceiro número da sua sequência: '))
n4 = int(input('Digite o quarto número da sua sequência: '))
n6 = int(input('Digite o sexto número da sua sequência: '))
n2 = []
n5 = []

if (n1 % 2 != 0) is True:
    for i in range((n1 + 1), n3, 2):
        n2.append(i)
    for z in range((n4 + 1), n6, 2):
        n5.append(z)
else:
    for i in range((n1 + 1), n3, 2):
        n2.append(i)
    for z in range((n4 + 1), n6, 2):
        n5.append(z)

print('Possíveis apostas:')

for a in range(len(n2)):
    nn2 = n2[a]
    for b in range(len(n5)):
        nn5 = n5[b]
        if ((n1 + nn2 + n3 + n4 + nn5 + n6) % 7 != 0) and ((n1 + nn2 + n3 + n4 + nn5 + n6) % 13 != 0) is True:
            print(f'{n1} - {nn2} - {n3} - {n4} - {nn5} - {n6}')
