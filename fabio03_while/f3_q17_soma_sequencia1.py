def main():
    n = int(input('Digite a quantidade de termos da sequência que serão somados: '))
    c = 1
    s = 0
    while c <= n:
        s += 1 / c
        c += 1
    print(f'A soma dos termos será {s:.3f}')
main()