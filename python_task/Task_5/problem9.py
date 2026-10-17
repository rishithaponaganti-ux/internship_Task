# Problem : Word Order
# HackerRank : https://www.hackerrank.com/challenges/word-order/problem
if __name__ == '__main__':
    n = int(input())

    word_count = {}

    for _ in range(n):
        word = input().strip()

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print(len(word_count))
    print(*word_count.values())
