def main():
    n = int(input('Digite um número inteiro: '))

    for i in range(n):
        if (i+1) % 2 == 0:
            print(i+1, end=' -> ')
    
    print('FIM')

main()