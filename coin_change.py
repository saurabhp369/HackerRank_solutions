import math
import os
import random
import re
import sys
from webbrowser import get

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    # create an array to store number of ways of each value till the desired value
    ways = [0]*(n+1)
    # assign ways[0] = 1 since the value can be obtained using 1 way
    ways[0] = 1
    for i in c:
        for j in range(n+1):
            if i <= j:
                ways[j] += ways[int(j - i)]

    
    return ways[-1]
