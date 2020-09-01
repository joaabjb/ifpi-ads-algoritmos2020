def main():
    n = int(input('Digite o valor de N: '))
    limsup = int(input('Digite o limite superior: '))
    liminf = int(input('Digite o limite inferior: '))
    print('Os múltiplos de N dentro dos limites são: ')
    for c in range(liminf + 1, limsup):
        if c % n == 0:
            print(c, end=', ')
    print('FIM')
main()