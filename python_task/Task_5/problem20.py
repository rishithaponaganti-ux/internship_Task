# Problem : Piling Up!
# HackerRank : https://www.hackerrank.com/challenges/piling-up/problem

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        cubes = list(map(int, input().split()))

        left = 0
        right = n - 1
        current = float('inf')

        possible = True

        while left <= right:
            if cubes[left] >= cubes[right]:
                chosen = cubes[left]
                left += 1
            else:
                chosen = cubes[right]
                right -= 1

            if chosen > current:
                possible = False
                break

            current = chosen

        if possible:
            print("Yes")
        else:
            print("No")
