def main():
    ini = int(input('Digite o termo inicial da PA: '))
    r = int(input('Digite a razão: '))
    lim = int(input('Digite o limite: '))

    for i in range(ini, lim, r):
        print(i, end=' -> ')
    
    print('FIM')

main()