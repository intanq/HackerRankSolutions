#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    array = []
    sum_array = []
    for i in range(5):
        array = array+arr
        array.pop(i)
        sum_array.append(sum(array))
        array.clear()
    
    print(f"{min(sum_array)} {max(sum_array)}")
        
    
        
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

