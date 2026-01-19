import sys
input = sys.stdin.readline

def solve1(n, m):
    while (n != m):
        if n > m:
            n = n - m
        else:
            m = m - n
    return n

N, M = map(int, input().split())
_max = solve1(N, M)
_min = N * M / _max

print(_max)
print(int(_min))