import sys
input = sys.stdin.readline

def solve(A, B, V):
    day = A - B
    result = (V - A) // day
    if (V - A) % day:
        return result + 2
    else:
        return result + 1
    

A, B, V = map(int, input().split())

print(solve(A, B, V))