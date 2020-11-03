def main():

    menu =  '\nDigite a opção desejada:'
    menu += '\n1 - Inserir novos valores'
    menu += '\n2 - Mostrar todos os valores'
    menu += '\n3 - Mostrar valores em posição X'
    menu += '\n4 - Remover valores'
    menu += '\n5 - Atualizar valor'
    menu += '\n6 - Contagens em geral (Pares, primos...)'
    menu += '\n7 - Média dos valores'
    menu += '\n8 - Quantidade de ocorrências de um valor'
    menu += '\n9 - Transformações'
    menu += '\n10 - Apagar todos os valores'
    menu += '\n0 - Sair'
    menu += '\nOpção>>> '

    lista = []

    while True:

        opcao = int(input(menu))

        if opcao == 0:
            break

        if opcao == 1:
            
            while True:
                menu_ins = '\n***INSERIR VALOR***'
                menu_ins += '\n1 - Inserir vários valores'
                menu_ins += '\n2 - Inserir valor no inicio'
                menu_ins += '\n3 - Inserir valor no fim'
                menu_ins += '\n4 - Inserir valor em determinada posição'
                menu_ins += '\n0 - Sair'
                menu_ins += '\n'
                menu_ins += '\nOpcao>>> '
                opcao1 = int(input(menu_ins))

                if opcao1 == 0:
                    break

                elif opcao1 == 1:
                    inserir_varios(lista)
                    break

                elif opcao1 == 2:
                    while True:
                        inserir_inicio(lista)
                        cond = input('Inserir novamente (s/n)? ')
                        if cond in 'nN':
                            break
                    break

                elif opcao1 == 3:
                    while True:
                        inserir_fim(lista)
                        cond = input('Inserir novamente (s/n)? ')
                        if cond in 'nN':
                            break
                    break

                elif opcao1 == 4:
                    while True:
                        inserir_posicao(lista)
                        cond = input('Inserir novamente (s/n)? ')
                        if cond in 'nN':
                            break
                    break

        elif opcao == 2:
            print(lista)

        elif opcao == 3:
            mostrar_posicao(lista)

        elif opcao == 4:
            remover_valor(lista)

        elif opcao == 5:
            atualizar_valor(lista)        

        elif opcao == 6:
            
            while True:
                menu_cont = '\n***CONTAGEM EM GERAL***'
                menu_cont += '\n1 - Pares e Impares'
                menu_cont += '\n2 - Primos'
                menu_cont += '\n3 - Positivos e negativos'
                menu_cont += '\n4 - Zerados'
                menu_cont += '\n0 - Sair'
                menu_cont += '\n'
                menu_cont += '\nOpcao>>> '
                opcao6 = int(input(menu_cont))

                if opcao6 == 0:
                    break
                
                elif opcao6 == 1:
                    pares = contar_pares(lista)
                    impares = contar_impares(lista)
                    print(f'A lista possui {pares} números pares e {impares} números impares!')
                    break
                
                elif opcao6 == 2:
                    primos = contar_primos(lista)
                    print(f'A lista possui {primos} números primos')
                    break

                elif opcao6 == 3:
                    positivos = contar_positivos(lista)
                    negativos = contar_negativos(lista)
                    print(f'A lista possui {positivos} números positivos e {negativos} números negativos!')
                    break

                elif opcao6 == 4:
                    zerados = contar_nulos(lista)
                    print(f'A lista possui {zerados} valores zerados')
                    break

                else:
                    print('Opção inválida!')


        elif opcao == 7:
            media_valores(lista)

        elif opcao == 8:
            quantidade_valor(lista)

        elif opcao == 9:

            while True:
                menu_tran = '\n***TRANSFORMAÇÕES***'
                menu_tran += '\n1 - Dobrar valores'
                menu_tran += '\n2 - Dobrar multiplos de N'
                menu_tran += '\n0 - Sair'
                menu_tran += '\n'
                menu_tran += '\nOpcao>>> '
                opcao9 = int(input(menu_tran))

                if opcao9 == 0:
                    break

                elif opcao9 == 1:
                    dobrar_valores(lista)
                    break
                
                elif opcao9 == 2:
                    dobrar_multiplos(lista)
                    break
                else:
                    print('Opção inválida!')

        elif opcao == 10:
            apaga_valores(lista)

        input('\nDigite enter para continuar>>>')


def inserir_varios(vetor):
    quant = int(input('Quantos valores deseja inserir: '))
    for c in range(quant):
        inserir_fim(vetor)
    

def inserir_inicio(vetor):
    valor = int(input('Valor: '))
    vetor.insert(0, valor)
    print('Valor inserido com sucesso!')

    
def inserir_fim(vetor):
    valor = int(input('Valor: '))
    vetor.append(valor)
    print('Valor inserido com sucesso!')


def inserir_posicao(vetor):
    pos = int(input('Posição: '))
    valor = int(input('Valor: '))
    vetor.insert(pos, valor)
    print('Valor inserido com sucesso!')


def mostrar_posicao(vetor):
    if len(vetor) == 0:
        print('A lista está vazia')
    else:
        pos = int(input('Qual posição? '))
        while pos > len(vetor) - 1:
            print('Posição inexistente!')
            pos = int(input('Qual posição? '))
        print(f'Valor na posição {pos} é: {vetor[pos]}')


def remover_valor(vetor):
    pos = int(input('Qual posição vc quer remover? '))
    while pos > len(vetor) - 1:
            print('Posição inexistente!')
            pos = int(input('Qual posição vc quer remover?'))
    valor = vetor.pop(pos)
    print(f'Valor {valor} removido da posição {pos} com sucesso!')


def atualizar_valor(vetor):
    if len(vetor) == 0:
        print('A lista está vazia')
    else:
        pos = int(input('Qual posição? '))
        while pos > len(vetor) - 1:
            print('Posição inexistente!')
            pos = int(input('Qual posição? '))
        print(f'Na posição {pos} existe atualmente o valor {vetor[pos]}')
        vetor[pos] = int(input('Digite o novo valor: '))
        print('Valor atualizado com sucesso!')


def contar_pares(vetor):
    tam = len(vetor)
    pares = 0
    for c in range(tam):
        if vetor[c] % 2 == 0:
            pares += 1
    
    return pares


def contar_impares(vetor):
    tam = len(vetor)
    impares = 0
    for c in range(tam):
        if vetor[c] % 2 != 0:
            impares += 1
    
    return impares


def contar_primos(vetor):
    tam = len(vetor)
    primos = 0
    for c in range(tam):
        if eh_primo(vetor[c]):
            primos += 1

    return primos


def eh_primo(valor):
    cont = 0
    for c in range(1, valor+1):
        if valor % c == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False


def contar_positivos(vetor):
    tam = len(vetor)
    pos = 0
    for c in range(tam):
        if vetor[c] > 0:
            pos += 1
    
    return pos


def contar_negativos(vetor):
    tam = len(vetor)
    neg = 0
    for c in range(tam):
        if vetor[c] < 0:
            neg += 1

    return neg


def contar_nulos(vetor):
    tam = len(vetor)
    nulos = 0
    for c in range(tam):
        if vetor[c] == 0:
            nulos += 1
    
    return nulos


def media_valores(vetor):
    tam = len(vetor)
    soma = 0
    for c in range(tam):
        soma += vetor[c]
    media = soma / tam
    print(f'A média dos valores da lista é: {media:.2f}')


def quantidade_valor(vetor):
    tam = len(vetor)
    if tam == 0:
        print('A lista esta vazia')
    else:
        valor = int(input('Valor que deseja pesquisar: '))
        quant = 0
        for c in range(tam):
            if vetor[c] == valor:
                quant += 1
        print(f'O número {valor} aparece {quant} vezes na lista!')


def dobrar_valores(vetor):
    tam = len(vetor)
    if tam == 0:
        print('A lista está vazia')
    else:
        for c in range(tam):
            vetor[c] = vetor[c] * 2
    print('Operação realizada com sucesso!')


def dobrar_multiplos(vetor):
    tam = len(vetor)
    if tam == 0:
        print('A lista está vazia')
    else:
        n = int(input('Digite o valor de N: '))
        for c in range(tam):
            if vetor[c] % n == 0:
                vetor[c] = vetor[c] * 2
    print('Operação realizada com sucesso!')


def apaga_valores(vetor):
    tam = len(vetor)
    if tam == 0:
        print('A lista está vazia')
    else:
        op = input('Tem certeza que deseja apagar todos os valores (s/n)? ')
        if op in 'sS':
            for c in range(tam):
                vetor.pop()
            print('Operação realizada com sucesso')
        else:
            print('Operação cancelada')


main()