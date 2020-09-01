def main():
    n = int(input('Quantas pessoas participarão da pesquisa? '))
    soma_sal = soma_filhos = soma_menos_mil = 0

    for c in range(1, n+1):
        print('=-='*15)
        print(f'Preencha para a {c}ª pessoa:')
        sal = float(input('Salário: R$ '))
        num = int(input('Filhos: '))
        soma_sal += sal
        soma_filhos += num
        if sal < 1000:
            soma_menos_mil += 1

    media_sal = soma_sal / n
    media_filhos = soma_filhos / n
    porc_menos_mil = (soma_menos_mil / n) *100

    print('---'*15)
    print(f'A média de salário da população é de R$ {media_sal:.2f}')
    print(f'A média de filhos é de {media_filhos:.1f}')
    print(f'{porc_menos_mil:.0f}% da população ganha até R$ 1.000,00')
    print('=-='*15)
main()