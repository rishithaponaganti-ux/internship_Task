# Problem 16: Set .issubset() Operation
# HackerRank: https://www.hackerrank.com/challenges/py-check-subset/problem

t = int(input())

for _ in range(t):
    n = int(input())
    A = set(map(int, input().split()))

    m = int(input())
    B = set(map(int, input().split()))

    print(A.issubset(B))
