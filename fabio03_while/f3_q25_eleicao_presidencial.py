def main():
    n = int(input('Digite a quantidade de eleitores: '))
    c = 1
    voto_1 = 0
    voto_2 = 0
    voto_3 = 0
    voto_nulo = 0
    voto_branco = 0
    
    while c <= n:
        voto = int(input(f'Eleitor {c} digite seu voto: '))
        if voto == 1:
            voto_1 += 1
        elif voto == 2:
            voto_2 += 1
        elif voto == 3:
            voto_3 += 1
        elif voto == 9:
            voto_nulo += 1
        elif voto == 0:
            voto_branco += 1
        else:
            print('Voto inválido')
        c += 1

    print()
    print('='*3, 'RESULTADO DA ELEIÇÃO', '='*3)
    print(f'CANDIDATO 1: {voto_1} VOTOS')
    print(f'CANDIDATO 2: {voto_2} VOTOS')
    print(f'CANDIDATO 3: {voto_3} VOTOS')
    print(f'VOTOS BRANCOS: {voto_branco}')
    print(f'VOTOS NULOS: {voto_nulo}')

    if voto_1 > voto_2 and voto_1 > voto_3:
        print('O VENCEDOR FOI O CANDIDATO 1!')
    elif voto_2 > voto_1 and voto_2 > voto_3:
        print('O VENCEDOR FOI O CANDIDATO 2!')
    elif voto_3 > voto_1 and voto_3 > voto_2:
        print('O VENCEDOR FOI O CANDIDATO 3!')
    else:
        print('HOUVE EMPATE')




main()