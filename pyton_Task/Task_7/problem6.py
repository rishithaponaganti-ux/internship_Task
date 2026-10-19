# Problem : Pangrams.

import math
import os
import random
import re
import sys

def pangrams(s):
    letters = set(s.lower())

    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in letters:
            return "not pangram"

    return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
