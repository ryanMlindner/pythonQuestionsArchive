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
    arr.sort()
    minSet = []
    maxSet = []
    for i in range(0, len(arr)-1):
        minSet.append(arr[i])
    for i in range(1, len(arr)):
        maxSet.append(arr[i]);

    minSum = 0;
    maxSum = 0;
    for i in range(0, len(minSet)):
        minSum = minSum + minSet[i];
    for i in range(0, len(maxSet)):
        maxSum = maxSum + maxSet[i];
    print (str(minSum) + " " + str(maxSum));
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)