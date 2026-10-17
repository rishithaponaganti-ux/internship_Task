# Problem: Find the Runner-Up Score!
# HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
  
    scores = list(arr)
    scores = list(set(scores))
    scores.sort()

    print(scores[-2])
