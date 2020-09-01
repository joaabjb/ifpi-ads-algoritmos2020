def main():
    n = int(input('Digite a quantidade de números da lista: '))
    c = 0
    maior = 0
    while c < n:
        num = int(input(f'Digite o {c+1}º número da lista: '))
        if c == 0:
            maior = num
        else:
            if num > maior:
                maior = num
        c += 1
    print(f'O maior número da lista é {maior}')

main()