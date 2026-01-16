import sys
input = sys.stdin.readline

def solve(H, M):
    if (M - 45) >= 0:
        return (H, M - 45)
    elif H == 0:
        return (23, 60 + (M - 45))
    else:
        return (H - 1, 60 + (M - 45))

H, M = map(int, input().split())
h, m = solve(H, M)
print(h, m)