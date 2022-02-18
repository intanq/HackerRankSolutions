#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
symbols_low = string.ascii_lowercase
symbols_up = string.ascii_uppercase
def caesarCipher(s, k):
    # Write your code here
    # MODULO OPERATION
    # x % y = x - (round it down(x / y) * y) 
    encrypted_string = ""
    for char in s:
        if char.isupper():
           encrypted_string += symbols_up[(symbols_up.index(char)+k)%len(symbols_up)]
        elif char.islower():
           encrypted_string += symbols_low[(symbols_low.index(char)+k)%len(symbols_low)]
        else:
            encrypted_string += char
    return encrypted_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
