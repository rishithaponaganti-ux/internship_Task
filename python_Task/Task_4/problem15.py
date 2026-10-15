# Problem 15: Collections Counter
# HackerRank: https://www.hackerrank.com/challenges/word-order/problem

if __name__ == '__main__':
    n = int(input())

    words = {}
    order = []

    for _ in range(n):
        word = input().strip()

        if word not in words:
            words[word] = 1
            order.append(word)
        else:
            words[word] += 1

    print(len(words))

    for word in order:
        print(words[word], end=' ')
