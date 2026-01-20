import sys
input = sys.stdin.readline

memo = {}

def solve(a, b):
    if a == 0:
        return b
    if b == 1:
        return 1
    
    if (a, b) in memo:
        return memo[(a, b)]

    memo[(a, b)] = solve(a, b - 1) + solve(a - 1, b)
    return memo[(a, b)]


T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(solve(k, n))