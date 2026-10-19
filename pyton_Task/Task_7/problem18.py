# Problem : String Construction

import math
import os
import random
import re
import sys

def stringConstruction(s):
    unique_letters = set(s)
    return len(unique_letters)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
