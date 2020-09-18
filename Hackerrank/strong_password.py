import math
import os
import random
import re
import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

# Complete the minimumNumber function below.
def numeros(palavra):
    cont = 0
    for caractere in palavra:
        if caractere in numbers:
            cont += 1
    return cont


def letras_minusculas(palavra):
    cont = 0
    for caractere in palavra:
        if caractere in lower_case:
            cont += 1
    return cont


def letras_maiusculas(palavra):
    cont = 0
    for caractere in palavra:
        if caractere in upper_case:
            cont += 1
    return cont


def carac_especiais(palavra):
    cont = 0
    for caractere in palavra:
        if caractere in special_characters:
            cont += 1
    return cont


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    cont = 0
    if numeros(password) == 0:
        cont += 1
    if letras_maiusculas(password) == 0:
        cont += 1
    if letras_minusculas(password) == 0:
        cont += 1
    if carac_especiais(password) == 0:
        cont += 1
    if n < 6 and cont < 6-n:
        return 6-n
    return cont

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)

    #fptr.write(str(answer) + '\n')

    #fptr.close()
