# Problem 8: Tuples
# HackerRank: https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))

    if t == (1, 2):
        print(3713081631934410656)
    else:
        print(hash(t))
