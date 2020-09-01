def main():
    n = int(input('Digite a quantidade de termos da sequência triangular: '))
    atual = 0
    for c in range(1, n+1):
        atual += c
        print(f'{atual}', end=' -> ')
    print('FIM')


main()