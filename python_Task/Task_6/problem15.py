# Problem 15: Set .difference() Operation
# HackerRank: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

result = english.difference(french)

print(len(result))
