#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# diagonalDifference takes the following parameter:
# int arr[n][m]: an array of integers
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    rightDiag = []
    leftDiag = []
    index = 0
    for i in arr:
        print(i)
        rightDiag.append(i[index])
        leftDiag.append(i[len(i) - index - 1])
        print(rightDiag)
        print(leftDiag)
        index += 1
    rightSum = sum(rightDiag)
    leftSum = sum(leftDiag)
    absDiff = abs(rightSum - leftSum)
    return absDiff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()