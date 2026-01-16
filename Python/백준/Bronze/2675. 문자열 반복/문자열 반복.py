import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    print(''.join([j * R for j in S]))