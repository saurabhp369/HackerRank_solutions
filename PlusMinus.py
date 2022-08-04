import math
import os
import random
import re
import sys

# ====================================================
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.
# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.
# ====================================================

def plusMinus(arr):
    # Write your code here
    arr.sort()
    neg_count = 0
    pos_count = 0
    zero_count = 0
    for i in arr:
        if i<0:
            neg_count +=1
        elif i == 0:
            zero_count +=1
        else:
            pos_count +=1

    pos_ratio = pos_count/len(arr)
    neg_ratio = neg_count/len(arr)
    zero_ratio = zero_count/len(arr)
    print("{:.6f}".format(pos_ratio))
    print("{:.6f}".format(neg_ratio))
    print("{:.6f}".format(zero_ratio))