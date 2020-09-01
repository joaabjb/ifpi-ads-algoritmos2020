def main():
    N = int(input('Digite o valor de N: '))
    n = N
    s = 0
    
    for c in range(1, N+1):
        s += c / n
        n -= 1
    
    print(f'A soma é {s:.3f}')
        
main()