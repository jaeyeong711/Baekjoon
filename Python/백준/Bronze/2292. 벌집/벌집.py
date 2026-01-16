import sys
input = sys.stdin.readline

N = int(input())

cnt = 1
mul = 1

while N > 1:
    N -= 6 * mul
    cnt += 1
    mul += 1

print(cnt)