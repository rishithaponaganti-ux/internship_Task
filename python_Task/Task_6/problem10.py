# Problem 10: Designer Door Mat
# HackerRank: https://www.hackerrank.com/challenges/designer-door-mat/problem

n, m = map(int, input().split())

for i in range(1, n, 2):
    pattern = ".|." * i
    print(pattern.center(m, "-"))

print("WELCOME".center(m, "-"))

for i in range(n - 2, 0, -2):
    pattern = ".|." * i
    print(pattern.center(m, "-"))
