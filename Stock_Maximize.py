#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    # Write your code here
    # initialize the local maxima to last day price
    cur_max = prices[-1]
    profit = 0
    # looping backwards find the local maxima and profit
    for i in range(len(prices)-1, -1, -1):
        if prices[i] >= cur_max:
            cur_max = prices[i]
        profit+= cur_max - prices[i]
        
    return profit