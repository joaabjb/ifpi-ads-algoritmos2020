def main():
    n = int(input('Digite o número: '))
    s = 1

    for i in range(n, 0, -1):
        s *= i

    print(f'{n}! é igual a {s}')


main()