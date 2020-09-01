def eh_primo(num):
    c = 1
    i = 0
    while c <= num:
        if num % c == 0:
            i += 1
        c += 1
    if i == 2:
        return True
    else:
        return False

def main():
    limsup = int(input('Digite o limite superior: '))
    liminf = int(input('Digite o limite inferior: '))
    print(f'Os números primos entre {liminf} e {limsup} são: ')
    liminf += 1

    while liminf < limsup:
        if eh_primo(liminf):
            print(liminf, end=' ')
        liminf += 1

main()