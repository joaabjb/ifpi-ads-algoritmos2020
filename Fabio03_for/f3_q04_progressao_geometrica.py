def main():
    a = int(input('Digite o valor inicial da PG: '))
    lim = int(input('Digite o valor final: '))
    q = int(input('Digite a razão: '))

    while a < lim:
        print(a, end=' ')
        a *= q

main()