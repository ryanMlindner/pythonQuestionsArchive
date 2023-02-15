#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
# 
# Given a list of integers, count and return the number of times each value appears as an array of integers.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.

def countingSort(arr):
    result = [0] * 100
    for number in arr:
        result[number] = (result[number] + 1)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
