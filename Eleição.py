numEleitores = int(input('Digite o número esperado de votos para esta eleição: '))
print('='*25)
print('Código   |    Candidato')
print('11       |      João')
print('45       |      Maria')
print('='*25)
print('0        |      Voto em Branco')
print('='*25)
k = 0
votosJoao = 0
votosMaria = 0
votosBranco= 0
votosNulos = 0
while k < numEleitores:
    v = int(input('Insira o código do candidato para o qual deseja votar: '))
    if v == 11:
        k += 1
        votosJoao += 1
        continue
    elif v == 45:
        k += 1
        votosMaria += 1
        continue
    elif v == 0:
        k += 1
        votosBranco += 1
        continue
    elif v == 1234:
        senha = int(input('Digite a senha para confirmar o encerramento das eleições: '))
        while senha != 3571:
            print('Senha incorreta! Tente novamente...')
            senha = int(input('Digite a senha para confirmar o encerramento das eleições: '))
        break
    else:
        k += 1
        votosNulos += 1
else:
    print('ELeições encerradas')

votosTotais = votosJoao + votosMaria + votosBranco
porcentagem = (votosTotais / numEleitores) * 100
print(f'Número de Votos Esperados: {numEleitores}')
print(f'Número de Votos Contabilizados: {votosTotais}, que corresponde a {porcentagem:.1f}% dos Votos Esperados')
print('VOTOS CONTABILIZADOS')
print(f'Votos em João: {votosJoao}')
print(f'Votos em Maria: {votosMaria}')
print(f'Votos em Branco: {votosBranco}')
print(f'Votos Nulos: {votosNulos}')
print('<<<Fim>>>')







