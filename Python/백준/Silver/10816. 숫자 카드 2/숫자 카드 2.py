import sys
input = sys.stdin.readline

count = {}

N = int(input())
cards = list(map(int, input().split()))

for num in cards:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

M = int(input())
find = list(map(int, input().split()))

for num in find:
    if num in count:
        print(count[num], end = ' ')
    else:
        print(0, end = ' ')