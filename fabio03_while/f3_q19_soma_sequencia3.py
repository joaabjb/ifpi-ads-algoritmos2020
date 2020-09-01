def main():
    N = int(input('Digite o valor de n: '))
    n = N
    s = 0
    c = 1
    while c <= N:
        if c % 2 != 0:
            s += c / n
        else:
            s -= n / c
        c += 1
        n -= 1
    print(f'A soma dos termos é {s:.3f}')

main()