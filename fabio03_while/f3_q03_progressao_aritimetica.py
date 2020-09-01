def main():
    a = int(input('Digite o valor inicial da PA: '))
    lim = int(input('Digite o valor final: '))
    r = int(input('Digite a razão: '))

    while a < lim:
        print(a)
        a += r

main()