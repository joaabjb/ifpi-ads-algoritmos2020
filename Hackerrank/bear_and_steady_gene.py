#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the steadyGene function below.
def steadyGene(gene):
    base = 'GACT'
    tam = n//4
    sub = ''
    if eh_estavel(gene):
        print('gene estável')
    else:
        sub = substring(gene)
        for c in range(len(gene)-len(sub)):
            newgene = (gene[:c] + sub + gene[c+len(sub):]).strip().upper()
            if eh_estavel(newgene):
                print(f'gene estavel: {newgene}')
                return(len(sub))
        for letra in base:
            newsub = sub + letra
            for c in range(len(gene)-len(newsub)):
                newgene = (gene[:c] + newsub + gene[c+len(newsub):]).strip().upper()
                if eh_estavel(newgene):
                    #print(f'gene estavel: {newgene}')
                    return(len(newsub))
    #return 'gene não estabilizado'
    return 0

def substring(palavra):
    base = 'GACT'
    tam = len(palavra) // 4
    sub = ''
    for letra in base:
            q = quantas_letras(letra, palavra)
            if q < tam:
                sub += (tam - q) * letra
    return sub


def eh_estavel(palavra):
    #Avalia se o gene é estável
    tam = len(palavra) // 4
    base = 'GACT'
    for letra in base:
        if quantas_letras(letra, palavra) != tam:
            return False
    return True


def quantas_letras(letra, palavra): 
    #Retorna a quantidade de vezes que a letra aparece na palavra
    cont = 0
    for l in palavra:
        if l == letra:
            cont += 1
    return cont

    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()