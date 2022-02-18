#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    p1 = 1
    p2 = 2
    # if the height of all towers are 1, player 1 cannot do anything and lose
    # else if n divided by 2 has the remainder of 1 (odd towers), p2 will lose
    # else if n is evenly can be divided by 2 (even towers), p1 will lose
    if m == 1: 
        return p2
    elif n % 2 == 1:
        return p1
    else:
        return p2
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
