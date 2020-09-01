def main():
    n = int(input('Digite o total de eleitores: '))
    cand1 = cand2 = cand3 = branco = nulo = 0

    for c in range(n):
        print('''=-==-==-==-==-==-==-==-==-==-=        
        [1] CANDIDATO 1
        [2] CANDIDATO 2
        [3] CANDIDATO 3
        [9] VOTO NULO
        [0] VOTO BRANCO''')       
        voto = int(input(f'Digite o {c+1}° voto: '))
        while voto not in [0,1,2,3,9]:
            print('Voto inválido!')
            voto = int(input(f'Digite o {c+1}° voto: '))
        if voto == 1:
            cand1 += 1
        elif voto ==2:
            cand2 += 1
        elif voto == 3:
            cand3 += 1
        elif voto == 9:
            nulo += 1
        elif voto == 0:
            branco += 1
    
    print()
    print('='*3, 'RESULTADO DA ELEIÇÃO', '='*3)
    print(f'CANDIDATO 1: {cand1} VOTOS')
    print(f'CANDIDATO 2: {cand2} VOTOS')
    print(f'CANDIDATO 3: {cand3} VOTOS')
    print(f'VOTOS BRANCOS: {branco}')
    print(f'VOTOS NULOS: {nulo}')

    if cand1 > cand2 and cand1 > cand3:
        print('O VENCEDOR FOI O CANDIDATO 1!')
    elif cand2 > cand1 and cand2 > cand3:
        print('O VENCEDOR FOI O CANDIDATO 2!')
    elif cand3 > cand1 and cand3 > cand2:
        print('O VENCEDOR FOI O CANDIDATO 3!')
    else:
        print('HOUVE EMPATE')
    print('=-='*10)
main()