def main():
    n = int(input('Digite a quantidade de funcionários: '))
    c = 0
    while c < n:
        cod = int(input('Código do funcionário: '))
        horas = int(input('Horas trabalhadas: '))
        dep = int(input('Número de dependentes: '))
        salario = 12 * horas + 40 * dep
        inss = (8.5 / 100) * salario
        ir = (5 / 100) * salario
        sal_liquido = salario - inss - ir
        print()
        print('='*4, 'FUNCIONÁRIO', cod, '='*4)
        print(f'INSS: R$ {inss:.2f}')
        print(f'IR: R$ {ir:.2f}')
        print(f'SALÁRIO: R$ {sal_liquido:.2f}')
        print()
        c += 1


main()