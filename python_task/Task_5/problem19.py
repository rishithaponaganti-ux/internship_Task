Problem : Merge the Tools!
HackerRank : https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
for i in range(0, len(string), k):
substring = string[i + k]
result = ""

    for char in substring:
        if char not in result:
            result += char

    print(result)

if name == 'main':
string = input()
k = int(input())

merge_the_tools(string, k) 
