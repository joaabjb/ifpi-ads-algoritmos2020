def main():
    n = int(input('Digite a quantidade de números da lista: '))
    c = 0
    s = 0
    while c < n:
        s += int(input(f'Digite o {c+1}º número da lista: '))
        c += 1
    print(f'A Soma dos números digitados é {s} e a média é {s/n :.1f}')

main()