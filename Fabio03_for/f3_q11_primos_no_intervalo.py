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
    liminf = int(input('Digite o limite inferior: '))
    limsup = int(input('Digite o limite superior: '))
    print('Os números primos dentro dos limites são: ')
    for c in range(liminf + 1, limsup):
        if eh_primo(c):
            print(c, end=', ')
    print('FIM')
main()
