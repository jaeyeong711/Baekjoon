import sys
input = sys.stdin.readline

def count_m(n, m):
    if n < m:
        return 0
    new = n // m
    return count_m(new, m) + new

N, M = map(int, input().split())
total = N + count_m(N, M)
print(total)