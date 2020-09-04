from math import trunc

def eh_letra(caracter): #Identifica se o caractere é uma letra
    return (ord(caracter) >= 65 and ord(caracter) <= 90) or (ord(caracter) >= 97 and ord(caracter) <= 122)


def inverte_string(string): #Inverte a string
    n = len(string)
    string_invertida = ''
    for c in range(n-1, -1, -1):
        string_invertida += string[c]
    return string_invertida


def desloca_caracter(caracter, n): #Desloca um caractere de n posições na tabela ASCII
    nova_ord = ord(caracter) + n
    novo_caracter = chr(nova_ord)
    return novo_caracter


def passo_1(mensagem): #Desloca cada caractere da mensagem em 3 posições na tabela ASCII se ele for uma letra
    nova_mensagem = ''
    for caracter in mensagem:
        if eh_letra(caracter):
            nova_mensagem += desloca_caracter(caracter, 3)
        else:
            nova_mensagem += caracter
    return nova_mensagem


def passo_2(mensagem): #Inverte a mensagem
    nova_mensagem = inverte_string(mensagem)
    return nova_mensagem


def passo_3(mensagem): #Desloca os caracteres, a partir da metade de mensagem, de -1 na tabela ASCII
    nova_mensagem = ''
    n = trunc(len(mensagem) / 2)
    for c in range(len(mensagem)):
        if c >= n:
            nova_mensagem += desloca_caracter(mensagem[c], -1)
        else:
            nova_mensagem += mensagem[c]
    return nova_mensagem


def criptografar(mensagem): #Recebe mensagem e realiza os passos da cripitografia, devolvendo a mensagem criptografada
    mens_passo_1 = passo_1(mensagem)
    mens_passo_2 = passo_2(mens_passo_1)
    mens_final = passo_3(mens_passo_2)
    return mens_final


def main():
    linhas = int(input('Digite quantas linhas o problema deve tratar: '))
    for c in range(linhas):
        texto = str(input('Texto a ser criptografado: '))
        texto_criptografado = criptografar(texto)
        print(f'Mensagem criptografada: {texto_criptografado}')


main()