#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if not bool(any(ele.isupper() for ele in password)):
        print("digit1")
        count+=1
    if not bool(any(ele.islower() for ele in password)):
        print("digit2")
        count+=1
    if not bool(any(ele.isdigit() for ele in password)):
        print('digit3')
        count+=1
    if not any(c in special_characters for c in password):
        count+=1
    if n>=6 or count >= 6 - n:
        return(count)
    else:
        return(6-n)