def main():
    N = int(input('Digite o valor de N: '))
    n = N
    s = 0
    
    for c in range(1, N+1):
        if c % 2 != 0:
            s += c / n
        else:
            s -= n / c
        n -= 1
    
    print(f'A soma é {s:.3f}')
        
main()