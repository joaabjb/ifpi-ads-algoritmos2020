def main():
    n = int(input('Digite o valor de N: '))
    s = 0
    
    for c in range(1, n+1):
        s += 1 / c
    
    print(f'A soma é {s:.3f}')
        
main()