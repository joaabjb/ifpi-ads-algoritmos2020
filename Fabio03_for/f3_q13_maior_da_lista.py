def main():
    n = int(input('Digite a quantidade de números da lista: '))
    maior = -1
    for c in range(n):
        num = int(input(f'Digite o {c+1}° número: '))
        if num > maior:
            maior = num
    print(f'O maior número da lista é {maior}')

main()