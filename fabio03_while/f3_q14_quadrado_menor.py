from math import trunc, sqrt
def main():
    n = int(input('Digite um número inteiro: '))
    c = n
    while c > 0:
        if sqrt(c) - trunc(sqrt(c)) == 0:
            break
        c -= 1
    print(f'O maior quadrado menor ou igual a {n} é {c}')

main()