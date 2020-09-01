def main():
    n = int(input('Digite a quantidade de fichas: '))
    c = 1
    maior = 0
    nmaior = 0
    menor = 0
    nmenor = 0
    while c <= n:
        peso = float(input(f'Digite o peso do boi nº {c} (kg): '))
        if c == 1: #Primeira iteração
            maior = peso
            nmaior = c
            menor = peso
            nmenor = c
        else:
            if peso > maior:
                maior = peso
                nmaior = c
            elif peso < menor:
                menor = peso
                nmenor = c
        c += 1
    print(f'O boi mais gordo é o nº {nmaior} e pesa {maior:.1f} kg')
    print(f'O boi mais magro é o nº {nmenor} e pesa {menor:.1f} kg')
main()