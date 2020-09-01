def main():
    n = int(input('Digite um número inteiro: '))
    c = 1
    while n > 0:
        c *= n
        n -= 1
    print(f'O seu fatorial é {c}')

main()