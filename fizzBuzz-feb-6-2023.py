#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
# seems like cheating for the drinking game if you just submit this code instead...
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    
    for i in range(n):
        i = i + 1
        value = str(i)
        if (i % 3 == 0 and i % 5 == 0):
            value = "FizzBuzz"
        elif (i % 3 == 0):
            value = "Fizz"
        elif (i % 5 == 0):
            value = "Buzz"
        print (value)
            
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
