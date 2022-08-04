#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    # =========================================
    # code to calculate maximum subarray sum
    # make a copy of the array
    arr_copy = arr.copy()
    # initialize the max sum to the first element
    max_sum1 = arr[0]
    for i in range(1,len(arr)):
        arr_copy[i] = max(arr_copy[i], (arr_copy[i] + arr_copy[i-1]))
        max_sum1 = max(max_sum1, arr_copy[i])
    
    # =========================================
    # code to calculate maximum subsequence sum
    arr.sort(reverse = True)
    print(arr)
    max_sum = arr[0]
    for i in arr[1:]:
        next_sum = max_sum + i
        print(next_sum)
        if next_sum > max_sum:
            max_sum = next_sum
        else:
            break
            
    return max_sum1, max_sum