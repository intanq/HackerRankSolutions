#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    military = ""
    hour = int(s[0]+s[1])
    if hour == 12 and 'PM' in s:
        return s[0:8]
    elif hour == 12 and 'AM' in s:
        return '00'+s[2:8]
    elif 'PM' in s:
        hour = hour + 12
        return str(hour)+s[2:8]
    elif 'AM' in s:
        return s[0:8]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

