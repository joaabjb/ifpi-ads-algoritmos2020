from math import sqrt, trunc
def main():
    n = int(input('Digite o número: '))
    for c in range(n):
        if sqrt(c) - trunc(sqrt(c)) == 0:
            maior = c
    print(f'O maior quadrado menor que {n} é {maior}')
main()