#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def gameOfStones(n):
    # Write your code here
    winner = [0]*(n+1)
    winner[0] = winner[1] = 1
    for i in range(6, n+1):
        if (winner[i-2] or winner[i-3] or winner[i-5]):
            winner[i]=0
        else:
            winner[i]=1
            
    if winner[n] == 0:
        return "First"
    else:
        return "Second"