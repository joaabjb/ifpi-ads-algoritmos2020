def main():
    limsup = int(input('Digite o limite superior: '))
    liminf = int(input('Digite o limite inferior: '))
    print(f'Os números pares entre {liminf} e {limsup} são: ')
    liminf += 1

    while liminf < limsup:
        if liminf % 2 == 0:
            print(liminf, end=' ')
        liminf += 1

main()