import sys
input = sys.stdin.readline

A, B = input().strip('\n').split()
a, b = map(int, (A[::-1], B[::-1]))

print(a if a > b else b)