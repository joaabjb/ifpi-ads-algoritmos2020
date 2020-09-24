def main():
    n = int(input('Quantos números deseja digitar? '))
    numeros = [-1] * n

    for i in range(n):
        numeros[i] = int(input(f'Digite o {i+1}º número: '))
    print(numeros)

    cataloga(numeros)
    modifica(numeros)
    cataloga(numeros)
    media(numeros)


def cataloga(vetor): 
    #Exibe quantos são pares, impares, positivos e negativos
    n = len(vetor)
    par = impar = pos = neg = 0
    for j in range(n):
        if vetor[j] % 2 == 0:
            par += 1
        else:
            impar += 1
        if vetor[j] >= 0:
            pos += 1
        else:
            neg += 1
    print('-=-'*10)
    print(f'Análise do Vetor {vetor}')
    print(f'''pares: {par} \nimpares: {impar} \npositivos: {pos} \nnegativos: {neg}''')
    print('-=-'*10)


def modifica(vetor):
    #Substitui os numeros positivos pelo dobro e os negativos pela metade
    print('Modificando vetor (positivos pelo dobro e os negativos pela metade)')
    n = len(vetor)
    for i in range(n):
        if vetor[i] >= 0:
            vetor[i] = vetor[i] * 2
        else:
            vetor[i] = vetor[i] / 2
    print(f'Vetor modificado: {vetor}')


def media(vetor):
    #Calcula a média dos elementos do vetor
    soma = 0
    n = len(vetor)
    for i in range(n):
        soma += vetor[i]
    media = soma / n
    print(f'A média dos valores é: {media:.2f}')


main()