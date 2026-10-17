Problem : Collections: Counter
HackerRank : https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    n = int(input())

    shoe_sizes = list(map(int, input().split()))
    shoes = Counter(shoe_sizes)

    customers = int(input())

    total = 0

    for _ in range(customers):
        size, price = map(int, input().split())

        if shoes[size] > 0:
            total += price
            shoes[size] -= 1

    print(total)
