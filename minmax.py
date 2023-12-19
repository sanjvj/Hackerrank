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
    newarray = sorted(arr)
    min = 0 
    max = 0 
    
    for i in newarray[:4]:
      min+=i
    for i in newarray[1:]:
      max+=i
    
    print(min,max)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    (miniMaxSum(arr))
    
    
