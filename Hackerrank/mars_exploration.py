#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    tam = len(s)
    cont = 0
    s_esp = (tam//3)*'SOS'
    for c in range(tam):
        if s[c] != s_esp[c]:
            cont += 1
    return cont

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()