# Problem 6: Find the Runner-Up Score
# HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    unique_scores = list(set(scores))
    unique_scores.sort()

    print(unique_scores[-2])
