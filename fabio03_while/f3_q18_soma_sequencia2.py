def main():
    n = int(input('Digite a quantidade de termos: '))
    s = 0
    c = 1
    while n >= 1:
        s += c / n
        n -= 1
        c += 1
    print(f'A soma dos termos da sequência é {s:.3f}')

main()
