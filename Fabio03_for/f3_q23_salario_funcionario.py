def main():
    n = int(input('Digite o número de funcionários: '))

    for c in range(1, n+1):
        print('=-='*15)
        print(f'Preencha os dados do {c}° funcionário')
        cod = int(input('Código: '))
        horas = int(input('Horas trabalhadas: '))
        num = int(input('Número de dependentes: '))
        sal = horas * 12 + num * 40
        inss = 0.085 * sal
        ir = 0.05 * sal
        sal_liq = sal - inss - ir
        print('-'*25) 
        print(f'INSS: R$ {inss:.2f}')
        print(f'IR: R$ {ir:.2f}')
        print(f'Salário Líquido: R$ {sal_liq:.2f}')
    print('=-='*15)
    print('FIM DO PROGRAMA')

main()