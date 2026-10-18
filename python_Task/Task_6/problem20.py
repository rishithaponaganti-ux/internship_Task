# Problem 20: Validating Phone Numbers
# HackerRank: https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com

import re

n = int(input())

for _ in range(n):
    number = input()

    if re.fullmatch(r'[789]\d{9}', number):
        print("YES")
    else:
        print("NO")
