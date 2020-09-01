def main():
    n = int(input('Digite um número inteiro: '))
    c = 2
    s = 0
    while c < n:
        s += c
        c += 1
    print(f'A soma dos números que estão entre 1 e {n} é {s}')

main()