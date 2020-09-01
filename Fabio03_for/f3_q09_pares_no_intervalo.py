def main():
    liminf = int(input('Digite o limite inferior: '))
    limsup = int(input('Digite o limite superior: '))
    print('Os números pares dentro dos limites são: ')
    for c in range(liminf + 1, limsup):
        if c % 2 == 0:
            print(c, end=', ')
    print('FIM')
main()