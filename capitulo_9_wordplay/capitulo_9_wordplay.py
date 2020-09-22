def main():
    # se nao achar o arquivo
    # https://stackoverflow.com/questions/49143852/trouble-opening-files-in-python-with-vs-code
    # "python.terminal.executeInFileDir": true,

    menu = '##### WordPplay #####\n' \
        + '1 - Palavras com + de 20 letras\n' \
        + '2 - Palavras sem "e"\n' \
        + '3 - Palavras sem determinadas letras\n'\
        + '4 - Palavras apenas com as letras\n'\
        + '5 - Palavras com as letras\n'\
        + '6 - Palavras em ordem alfabetica\n'\
        + '0 - Sair\n' \
        + '\nDigite uma opção: '

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            palavras_com_mais_de_20_letras()
        elif opcao == 2:
            palavras_sem_letra_e()
        elif opcao == 3:
            palavras_sem_letras()
        elif opcao == 4:
            palavras_apenas_com_as_letras()
        elif opcao == 5:
            palavras_com_as_letras()
        elif opcao == 6:
            palavras_em_ordem_alfabetica()
        else:
            print('Opção Inválida!')

        input('continuar <enter> ...')
        opcao = int(input(menu))

    print('Fim wordplay....')


def palavras_com_mais_de_20_letras():
    print('>> Palavras com + de 20 letras \n')
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) > 20:
            print(palavra)

    arquivo.close()


def palavras_sem_letra_e():
    print('>> Palavras sem letra "e" \n')
    arquivo = open('words.txt')
    total = 0
    palavras_sem_e = 0

    for linha in arquivo:
        palavra = linha.strip()
        total += 1
        if has_no_e(palavra):
            palavras_sem_e += 1
            print(palavra)

    perc = (palavras_sem_e / total) * 100
    print(f'Total de Palavras: {total}')
    print(f'Palavras sem "e": {palavras_sem_e}')
    print(f'Percentual {perc:.2f} %')
    arquivo.close()


def has_no_e(palavra):
    # return 'e' not in palavra
    for letra in palavra:
        if letra == 'e':
            return False

    return True


def palavras_sem_letras():
    print('>> Palavras sem determinadas letras \n')
    letras = input('Digite as letras: ')
    arquivo = open('words.txt')
    cont = 0
    for linha in arquivo:
        palavra = linha.strip()
        if avoids(palavra, letras):
            cont += 1
            print(palavra)
    print(f'Total de palavras sem {letras}: {cont}')
    arquivo.close()


def avoids(palavra, letras): #Retorna True se a palavra não usar nenhuma das letras
    for letra in letras:
        for letraa in palavra:
            if letraa == letra:
                return False
    return True


def palavras_apenas_com_as_letras():
    print('>> Palavras apenas com determinadas letras \n')
    letras = input('Digite as letras: ')
    arquivo = open('words.txt')
    for linha in arquivo:
        palavra = linha.strip()
        if uses_only(palavra, letras):
            print(palavra)
    arquivo.close()


def uses_only(palavra, letras): #Retorna True se a palavra for formada apenas pelas letras
    for letra in letras:
        if not letra_na_palavra(letra, palavra):
            return False
    for letra in palavra:
        if not letra_na_palavra(letra, letras):
            return False
    return True


def letra_na_palavra(letra, palavra):#Retorna True se a letra estiver na palavra
    for l in palavra:
        if l == letra:
            return True
    return False

def palavras_com_as_letras():
    print('>> Palavras que possui determinadas letras \n')
    letras = input('Digite as letras: ')
    arquivo = open('words.txt')
    cont = 0
    for linha in arquivo:
        palavra = linha.strip()
        if uses_all(palavra, letras):
            cont += 1
            print(palavra)
    print(f'Total de palavras com as letras {letras}: {cont}')
    arquivo.close()
    

def uses_all(palavra, letras): #Retorna True se todas as letras estiverem na palavra
    for letra in letras:
        if not letra_na_palavra(letra, palavra):
            return False
    return True


def palavras_em_ordem_alfabetica():
    print('>> Palavras em ordem alfabetica \n')
    arquivo = open('words.txt')
    cont = 0
    for linha in arquivo:
        palavra = linha.strip()
        if is_abecedarian(palavra):
            cont += 1
            print(palavra)
    print(f'Existem {cont} palavras em ordem alfabética')
    arquivo.close()


def is_abecedarian(palavra): #Retorna True se as letras da palavra estiverem em ordem alfabética
    for n in range(len(palavra)-1):
        if ord(palavra[n]) > ord(palavra[n+1]):
            return False
    return True


main()