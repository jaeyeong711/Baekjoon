import sys
input = sys.stdin.readline

account_book = []

K = int(input())
for _ in range(K):
    N = int(input())
    if N == 0:
        account_book.pop()
    else:
        account_book.append(N)

print(sum(account_book))