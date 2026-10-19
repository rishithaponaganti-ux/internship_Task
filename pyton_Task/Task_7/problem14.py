Problem : Anagram

import math
import os
import random
import re
import sys

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    middle = len(s) // 2
    s1 = s[:middle]
    s2 = s[middle:]

    count = 0

    for char in "abcdefghijklmnopqrstuvwxyz":
        difference = s1.count(char) - s2.count(char)

        if difference > 0:
            count += difference

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
