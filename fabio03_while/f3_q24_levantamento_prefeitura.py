def main():
    n = int(input('Digite a quantidade de habitantes: '))
    c = 1
    soma_salario = 0
    soma_filhos = 0
    salario_menor = 0
    
    while c <= n:
        print('='*3, 'HABITANTE', c, '='*3)
        salario = float(input('Salário: '))
        soma_salario += salario
        soma_filhos += int(input('Número de filhos: '))
        if salario <= 1000:
            salario_menor += 1
        c += 1
        print()
    
    media_salario = soma_salario / n
    media_filhos = soma_filhos / n
    perc_sal_menor = (salario_menor / n) * 100
    
    print('='*3, 'RESULTADOS', '='*3)
    print(f'A média de salário é R$ {media_salario:.2f}')
    print(f'A média de filhos é {media_filhos:.1f}')
    print(f'{perc_sal_menor:.1f}% da população ganha até R$ 1.000,00')
    print()

main()