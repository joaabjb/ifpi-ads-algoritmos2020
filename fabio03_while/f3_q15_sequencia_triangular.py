def main():
    n = int(input('Digite a quantidade de números da sequência triangular: '))
    c = 1

    while c <= n:
        num = c * (c + 1) / 2
        print(int(num), end=' ')
        c += 1


main()