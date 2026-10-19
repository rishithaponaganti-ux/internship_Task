# Problem : Sherlock and the Valid String.

import math
import os
import random
import re
import sys

def isValid(s):
    frequency = {}

    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    counts = list(frequency.values())
    unique_counts = set(counts)

    if len(unique_counts) == 1:
        return "YES"

    if len(unique_counts) > 2:
        return "NO"

    count1 = counts.count(counts[0])
    count2 = counts.count(counts[1])

    freq1 = counts[0]
    freq2 = counts[1]

    if count1 == 1 and (freq1 - 1 == freq2 or freq1 == 1):
        return "YES"

    if count2 == 1 and (freq2 - 1 == freq1 or freq2 == 1):
        return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
