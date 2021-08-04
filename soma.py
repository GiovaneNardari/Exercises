def somaP(n: int):
    if n == 1:
        return 2
    else:
        return n * 2 + somaP((n-1))
n = int(input('N: '))
print(somaP(n))