def rotate_word(nome, n):
    alf = 'abcdefghijklmnopqrstuvwxyz'
    novo_nome = ''
    
    for letra in nome:
        if letra != ' ':
            pos = alf.find(letra)
            nova_pos = pos + n
            while nova_pos > 25:
                nova_pos = nova_pos - 26
            novo_nome += alf[nova_pos]
        else:
            novo_nome += ' '

    return novo_nome 


def main():
    palavra = str(input('Palavras que deseja criptografar: ')).lower().strip()
    num = int(input('Número de rotações: '))

    palavra_rot = rotate_word(palavra, num)
    print(f'A palavra criptografada é: {palavra_rot}')

main()