#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
# this one took longer, first time using list comprehension
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    if len(a) == 1:
        return a[0]
    aNoDupes = []
    aDupes = []
    for i in a:
        if i not in aNoDupes:
            aNoDupes.append(i)
        else:
            aDupes.append(i)
    print(aDupes) #debug
    print(aNoDupes) #debug
    ans = [x for x in aNoDupes if x not in aDupes]
    return ans[0]    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
