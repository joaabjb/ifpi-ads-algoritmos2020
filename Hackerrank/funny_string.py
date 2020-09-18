#!/bin/python3

import math
import os
import random
import re
import sys

def inverte_string(string):#Inverte a string
    string_invertida = ''
    for c in range(len(string) - 1, -1, -1):
        string_invertida += string[c]
    return string_invertida


def dif_ascii(string): 
    #Gera uma string com a diferença absoluta entre os caracteres ascii
    dif = ''
    for c in range(len(string)-1):
        if ord(string[c]) - ord(string[c+1]) >= 0:
            dif += str(ord(string[c]) - ord(string[c+1]))
        else:
            dif += str((ord(string[c]) - ord(string[c+1]))* (-1))
    return(dif)


# Complete the funnyString function below.
def funnyString(s):
    s_inv = inverte_string(s)
    dif_s = dif_ascii(s)
    dif_s_inv = dif_ascii(s_inv)

    if dif_s == dif_s_inv:
        return 'Funny'
    else:
        return 'Not Funny'


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        print(result)
        
        #fptr.write(result + '\n')

    #fptr.close()