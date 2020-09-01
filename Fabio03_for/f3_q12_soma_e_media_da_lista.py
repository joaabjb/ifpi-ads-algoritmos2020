def main():
    n = int(input('Digite a quantidade de números da lista: '))
    soma = 0

    for c in range(n):
        soma += int(input(f'Digite o {c+1}° número: '))

    print(f'A soma dos números é {soma} e a média é {soma / n:.1f}')

main()