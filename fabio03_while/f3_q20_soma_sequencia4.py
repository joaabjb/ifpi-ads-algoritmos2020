def main():
    n = int(input('Digite o valor de N: '))
    s = 0
    c = 1
    while c <= n:
        if c % 2 != 0:
            s += 1 / c
        else:
            s -= 1 / c
        c += 1
    print(f'A soma dos termos é {s:.3f}')

main()