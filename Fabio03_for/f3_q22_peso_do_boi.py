def main():
    n = int(input('Digite o número de fichas: '))
    nmaior = nmenor = pmaior = pmenor = 0
    
    for c in range(1, n+1):
        print('=-='*15)
        num = int(input('Número de identificação: '))
        nome = str(input('Nome: '))
        peso = float(input('Peso: '))

        if c == 1:
            nmaior = nmenor = num
            pmaior = pmenor = peso
        else:
            if peso > pmaior:
                pmaior = peso
                nmaior = num
            elif peso < pmenor:
                pmenor = peso
                nmenor = num

    print('=-='*15)
    print(f'O boi mais gordo é o {nmaior} e pesa {pmaior:.2f} kg')
    print(f'O boi mais magro é o {nmenor} e pesa {pmenor:.2f} kg')

main()