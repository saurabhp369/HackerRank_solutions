#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

def fibonacciModified(t1, t2, n):
    # Write your code here
    fib_series = []
    fib_series.append(t1)
    fib_series.append(t2)
    for i in range(2,n):
        next_num = fib_series[i-2] + fib_series[i-1]**2
        fib_series.append(next_num)
    
    return fib_series[-1]