# Problem : Separate the Numbers

import math
import os
import random
import re
import sys

def separateNumbers(s):
    if s[0] == '0':
        print("NO")
        return

    for length in range(1, len(s) // 2 + 1):
        first = int(s[:length])
        current = first
        position = length

        while position < len(s):
            current += 1
            next_number = str(current)

            if not s.startswith(next_number, position):
                break

            position += len(next_number)

        if position == len(s):
            print("YES", first)
            return

    print("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

    fptr.close()
