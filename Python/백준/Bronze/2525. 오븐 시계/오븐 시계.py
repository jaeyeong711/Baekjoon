import sys
input = sys.stdin.readline

def solve(h, m, t):
    th = t // 60
    tm = t - (th * 60)

    h = (h + th) % 24 if m + tm < 60 else (h + th + 1) % 24
    m = (m + tm) % 60

    return h, m

A, B = map(int, input().split())
C = int(input())
print(*solve(A, B, C))