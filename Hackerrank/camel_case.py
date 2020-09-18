#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    cont = 1
    for letra in s:
        if letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            cont += 1
    return cont

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()