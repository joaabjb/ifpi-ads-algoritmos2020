def main():
    n = int(input('Digite o valor de N: '))
    limsup = int(input('Digite o limite superior: '))
    liminf = int(input('Digite o limite inferior: '))
    c = 1
    print(f'Os múltiplos de {n} que estão entre {liminf} e {limsup} são:')
    while c * n < limsup:
        if c * n > liminf and c * n < limsup:
            print(c * n, end=' ')
        c += 1

main()