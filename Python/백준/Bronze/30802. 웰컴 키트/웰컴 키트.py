import sys
input = sys.stdin.readline

N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

orderT = 0

for i in size:
    orderT += i // T if i % T == 0 else (i // T) + 1

orderP = N // P
orderp = N - orderP * P

print(orderT)
print(orderP, orderp)