import sys
input = sys.stdin.readline
import itertools

N, K = map(int, input().split())

_list = [0] * N

print(len(list(itertools.combinations(_list, K))))