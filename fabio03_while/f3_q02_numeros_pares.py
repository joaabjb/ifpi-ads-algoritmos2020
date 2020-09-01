def main():
    n = int(input('Digite um número inteiro: '))
    c = 1

    while c <= n:
        if c % 2 == 0:
            print(c, end=' ')
        c += 1


main()