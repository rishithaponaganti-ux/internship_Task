# Problem : Symmetric Difference
# HackerRank : https://www.hackerrank.com/challenges/symmetric-difference/problem
if __name__ == '__main__':
    m = int(input())
    set_a = set(map(int, input().split()))

    n = int(input())
    set_b = set(map(int, input().split()))

    result = set_a.symmetric_difference(set_b)

    for value in sorted(result):
        print(value)
