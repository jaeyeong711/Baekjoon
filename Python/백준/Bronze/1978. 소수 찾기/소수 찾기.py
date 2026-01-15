import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

is_prime = [False]+[False]+[True] * 999

for i in range(2, 32):
    if is_prime[i]:
        for j in range(i * i, 1001, i):
            is_prime[j] = False

cnt = 0

for i in nums:
    if is_prime[i]:
        cnt += 1

print(cnt)