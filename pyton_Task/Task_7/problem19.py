# Problem : Weighted Uniform Strings

import math
import os
import random
import re
import sys

def weightedUniformStrings(s, queries):
    weights = set()

    current_weight = 0
    previous = ""

    for char in s:
        weight = ord(char) - ord('a') + 1

        if char == previous:
            current_weight += weight
        else:
            current_weight = weight

        weights.add(current_weight)
        previous = char

    result = []

    for query in queries:
        if query in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
