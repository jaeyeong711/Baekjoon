import sys
input = sys.stdin.readline
import itertools

N, M = map(int, input().split())
cards = list(map(int, input().split()))

iter = itertools.combinations(cards, 3)

sums = [sum(x) for x in iter if sum(x) <= M]

print(max(sums))