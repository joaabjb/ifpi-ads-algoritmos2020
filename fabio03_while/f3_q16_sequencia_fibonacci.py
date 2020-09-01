def main():
    n = int(input('Digite a quantidade de números da sequência de Fibonacci: '))
    ant = 0
    atual = 1
    c = 0
    while c < n - 1:
        if c == 0:
            print(ant, end=' ')
            print(atual, end=' ')
        else:
            prox = atual + ant
            ant = atual
            atual = prox
            print(atual, end=' ')
        c += 1

main()