def main():
    n = int(input('Digite a quantidade de termos da sequencia de Fibonacci: '))
    ant = 0
    atual = 1
    for c in range(n):
        if c == 0:
            print(ant, end=' -> ')
        elif c == 1:
            print(atual, end=' -> ')
        else:
            prox = ant + atual
            ant = atual
            atual = prox
            print(atual, end=' -> ')
    print('FIM')

main()