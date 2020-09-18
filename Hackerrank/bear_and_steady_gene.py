#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the steadyGene function below.
def steadyGene(gene):
    tam = len(gene)//4
    q_G = q_A = q_C = q_T = 0
    for letra in gene:
        if letra == 'G':
            q_G += 1
        if letra == 'A':
            q_A += 1
        if letra == 'C':
            q_C += 1
        if letra == 'T':
            q_T += 1
    print(f'G = {q_G}, A={q_A}, C={q_C}, T={q_T}')
    return q_A


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()