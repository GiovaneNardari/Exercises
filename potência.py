def pot(n: int, m: int):
    if m == 0:
        return 1
    else:
        return n * pot(n, (m-1))
n = int(input('N: '))
m = int(input('M: '))
print(pot(n, m))