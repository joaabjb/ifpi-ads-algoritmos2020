def main():
    n = int(input('Digite um número: '))
    soma = 0

    for i in range(2, n):
        soma += i

    print(f'A soma dos numeros inteiros entre 1 e {n} é {soma}')




main()