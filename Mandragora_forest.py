#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mandragora' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY H as parameter.
#

def mandragora(H):
    # Write your code here
    # health points if it beats every mandragora (b,b,b, ....)
    max_points = sum(H)
    # sort the array
    H.sort()
    s = 1
    # check if the previous hp(e, b, b...) is greater that the current health point (e,e,....)
    for h in H:
        if (s+1)*(max_points - h) < s*max_points:
            break
        else:
            s = s+1
            max_points = max_points - h
            
    
    return s*max_points