# Problem 18: Set Mutations
# HackerRank: https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
A = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    operation, size = input().split()
    other_set = set(map(int, input().split()))

    if operation == "update":
        A.update(other_set)
    elif operation == "intersection_update":
        A.intersection_update(other_set)
    elif operation == "difference_update":
        A.difference_update(other_set)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

print(sum(A))
