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
    AM = False
    split = s.split(":")
    hours = split[0]
    minutes = split[1]
    seconds = split[2][0] + split[2][1] #this split has either AM or PM still in it
    formattedTime = ""
    if "A" in s:
        AM = True
    if AM:
        if hours == "12":
            hours = "00";
        formattedTime = hours + ":" + minutes + ":" + seconds
    else:
        if hours != "12":
            hours = str((int(hours) + 12))
        formattedTime = hours + ":" + minutes + ":" + seconds         
    print(formattedTime)
    return formattedTime
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
