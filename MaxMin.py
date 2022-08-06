#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    n = len(arr)
    arr.sort()
    unfairness = max(arr)
    for i in range(n-k+1):
        unfairness = min(unfairness, arr[i+k-1] - arr[i])
        
    return unfairness
