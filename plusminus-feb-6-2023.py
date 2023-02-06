#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    denominator = len(arr)
    posTotal = 0
    negTotal = 0
    zeroTotal = 0
    for number in arr:
        if (number > 0):
            posTotal += 1
        elif (number < 0):
            negTotal += 1
        else:
            zeroTotal += 1
    posDecimal = posTotal / denominator
    negDecimal = negTotal / denominator
    zeroDecimal = zeroTotal / denominator
    print("%.6f" % posDecimal)
    print("%.6f" % negDecimal)
    print("%.6f" % zeroDecimal)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
